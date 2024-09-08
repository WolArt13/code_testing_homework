import pytest
import json
import os
import app

def get_data():
    with open('fixtures/directories.json', 'r', encoding='utf-8') as file:
        directories = json.load(file)
    with open('fixtures/documents.json', 'r', encoding='utf-8') as file:
        documents = json.load(file)

    return directories, documents

directories, documents = get_data()

def format_documents(docs):
    formatted_documents = list()
    for document in documents:
        doc_type = document['type']
        doc_number = document['number']
        doc_owner_name = document['name']
        formatted_documents.append('{} "{}" "{}"'.format(doc_type, doc_number, doc_owner_name))
    return formatted_documents

class TestApp:

    def setup(self):
        print('Setup...')
    
    def teardown(self):
        directories, documents = get_data()
        print('Teardown...')

    def test_get_all_documents_info(self):
        assert app.show_all_docs_info() == format_documents(documents)

    def test_find_document_success(self):
        assert app.check_document_existance('2207 876234') == True

    def test_find_document_fail(self):
        assert app.check_document_existance('12345678') == False

    def test_error_delete_doc(self):
        assert app.delete_doc('65549848') == False and app.check_document_existance('65549848') == False

    def test_success_delete_doc(self):
        assert app.delete_doc('2207 876234') == True and app.check_document_existance('2207 876234') == False

    def test_add_new_doc(self):
        doc_number = '15579842'
        doc_type = 'passport'
        doc_owner_name = 'Иванов Иван'
        documents.append({'type': doc_type, 'number': doc_number, 'name': doc_owner_name})
        app.add_new_doc(doc_number, doc_type, doc_owner_name, '365')
        assert app.check_document_existance(doc_number) == True

if __name__ == '__main__':
    pytest.main()