from os import path


class Routine:
    """

    Attributes
    ----------
    dataset : bqup.dataset.Dataset
    bq_routine : bigquery.routine.RoutineListItem
    """
    routine_query = ''
    is_function = False

    def __init__(self, dataset, bq_routine):
        self.dataset = dataset
        routine = dataset.project.client.get_routine(bq_routine.reference)
        self.is_function = routine.type_ == 'SCALAR_FUNCTION'
        self.routine_type = 'function' if self.is_function else 'procedure'
        self.routine_id = routine.routine_id
        print(f'\t\tLoading routine {bq_routine.reference}...')
        self.routine_query = self._get_create_or_replace(routine)

    def _get_create_or_replace(self, routine):
        return 'CREATE OR REPLACE ' + self.routine_type.upper() + " `" + self._get_full_name(routine) + "`(" \
               + self._get_arguments(routine) + ")" \
               + self._get_return(routine) \
               + self._get_language(routine) \
               + self._get_options(routine) \
               + self._get_body(routine) + ";"

    def _get_arguments(self, routine):
        arguments_str = ''
        arguments = routine.to_api_repr()['arguments']
        if len(arguments) > 0:
            arguments_str = ', '.join((self._get_parameter(argument) for argument in arguments))
        return arguments_str

    def _get_parameter(self, argument):
        name = argument['name']
        mode = ''
        if 'mode' in argument:
            mode = f'{argument["mode"]} '
        return f'{mode}{name} {self._get_arg(argument["dataType"])}'

    def _get_options(self, routine):
        return ' '  # not implemented!

    def _get_full_name(self, routine):
        return f'{routine.reference}'

    def _get_return(self, routine):
        routine_data = routine.to_api_repr()
        if 'returnType' in routine_data:
            return_type = routine_data['returnType']
            if return_type is not None:
                return f' RETURNS {self._get_arg(return_type)}'
        return ' '

    def _is_nested(self, type):
        return type == 'ARRAY' or type == 'STRUCT'

    def _get_arg(self, return_type):
        return_string = ''
        type_kind = return_type['typeKind']
        if self._is_nested(type_kind):
            if type_kind == 'ARRAY':
                return_string = f'{type_kind}<{self._get_arg(return_type["arrayElementType"])}>'
            if type_kind == 'STRUCT':  # STRUCT<event_category STRING, event_action STRING>
                return_string = f'{type_kind}<{self._get_struct_arg(return_type["structType"])}>'
        else:
            return_string = type_kind
        return return_string

    def _get_struct_arg(self, struct_type):
        return ', '.join((self._get_struct_field(field) for field in struct_type['fields']))

    def _get_struct_field(self, field):
        return f'{field["name"]} {self._get_arg(field["type"])}'

    def _get_language(self, routine):
        language = ''
        if routine.language == 'JAVASCRIPT':
            language = ' LANGUAGE js'
        return language

    def _get_body(self, routine):
        body = routine.body
        separator_start = '"""'
        separator_end = '"""'
        if routine.language == 'SQL':
            separator_start = '('
            separator_end = ')'
        return f'AS {separator_start} \n {body.strip()} \n {separator_end}'

    def _get_export_file_extension(self):
        """Get the file extension for the export file of this routine.

        Returns
        -------
        str
            The file extension (i.e. "sql")
        """
        return 'sql'

    def _get_export_routine_path(self, dataset_dir):
        """Get the export path for this routine

        Parameters
        ----------
        dataset_dir : str
            Directory where dataset will be saved

        Returns
        -------
        str
            The export path
        """
        routine_file_name = f'{self.routine_id}.{self.routine_type}.{self._get_export_file_extension()}'
        return path.join(dataset_dir, routine_file_name)

    def to_file_contents(self) -> str:
        return self.routine_query

    def print_info(self):
        """Print information about the routine
        """
        print(f'\t\t[{self.routine_type}] {self.routine_id} ({len(self.routine_query)} bytes)')

    def export(self, dataset_dir):
        """Export routine to specified directory as either an "sql" or "json" file

        Parameters
        ----------
        dataset_dir : str
            Directory where dataset will be saved
        """
        routine_path = self._get_export_routine_path(dataset_dir)
        with open(routine_path, 'w', encoding='utf-8') as f:
            f.write(self.to_file_contents())
