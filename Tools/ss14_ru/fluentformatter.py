#!/usr/bin/env python3

# Um formatador que alinha arquivos fluentes (.ftl) com o guia de estilo
# path - caminho para a pasta que contém os arquivos a serem formatados. Para formatar todo o projeto, você precisa substituir o valor por root_dir_path
import typing

from file import FluentFile
from project import Project
from fluent.syntax import ast, FluentParser, FluentSerializer


######################################### Class defifitions ############################################################

class FluentFormatter:
    @classmethod
    def format(cls, fluent_files: typing.List[FluentFile]):
        for file in fluent_files:
            file_data = file.read_data()
            parsed_file_data = file.parse_data(file_data)
            serialized_file_data = file.serialize_data(parsed_file_data)
            file.save_data(serialized_file_data)

    @classmethod
    def format_serialized_file_data(cls, file_data: typing.AnyStr):
        parsed_data = FluentParser().parse(file_data)

        return FluentSerializer(with_junk=True).serialize(parsed_data)



######################################## Var definitions ###############################################################
project = Project()
fluent_files = project.get_fluent_files_by_dir(project.ru_locale_dir_path)

########################################################################################################################

FluentFormatter.format(fluent_files)
