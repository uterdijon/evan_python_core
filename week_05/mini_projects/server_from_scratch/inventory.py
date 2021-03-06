import json
import sys

class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        address = environ['REMOTE_ADDR']
        fileinfo = self.filereader()
        words = self.word_list(query)

        if method == 'GET' and path == '/inventory':
            inven = json.dumps(fileinfo)
            return inven

        elif method == 'POST' and path == '/inventory':
            self.create_product(words, fileinfo)
            self.display_status(fileinfo, words)

        elif method == 'PATCH' and path == '/inventory':
            self.augment_quantity(words, fileinfo)
            self.display_status(fileinfo, words)

        elif method == 'DELETE' and path == '/inventory':
            self.delete_product(words, fileinfo)
            return f'There are currently 0 {words[0][1]} in the inventory.'



    def create_product(self, words, fileinfo):
        if words[0][1] in fileinfo:
                return 'This item is already in the inventory.'
        else:
                fileinfo[words[0][1]] = 0
        self.filewriter(fileinfo)

    def delete_product(self, words, fileinfo):
        if words[0][1] in fileinfo:
            del fileinfo[words[0][1]]
        else:
            return 'This item is not in the inventory.'
        self.filewriter(fileinfo)

    def augment_quantity(self, words, fileinfo):
        if words[0][1] in fileinfo:
            fileinfo[words[0][1]] += int(words[1][1])
        else:
            return f'There is no such item {words[0][1]} in the inventory. Please add it.'
        self.filewriter(fileinfo)

    def display_status(self, fileinfo, words):
        return f'There are currently {fileinfo[words[0][1]]} {words[0][1]} in the inventory.'

    def word_list(self, query):
        words = []
        for pair in query.split('&'):
            one_word = pair.split('=')
            words.append(one_word)
            return words

    def filewriter(self, fileinfo):
        json.dump(fileinfo, open('/Users/evan/CodingNomads/python_core/week_05/mini_projects/server_from_scratch/inventory_api.txt', 'w'))
        return 'Your inventory has been updated'

    def filereader(self):
        _dict = {}
        with open('/Users/evan/CodingNomads/python_core/week_05/mini_projects/server_from_scratch/inventory_api.txt', 'r') as f:
            _dict = json.loads(f.read())
        return _dict
