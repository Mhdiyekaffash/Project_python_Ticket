path_file = "test.csv"

import csv
import os


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as myfile:
                reader = csv.DictReader(myfile)
                return list(reader)
        else:
            return False

    def write_file(self, info, mode="a"):
        if isinstance(info, dict):
            # if self.check_unique_id(info["id"]):
            #     return "id already exists"
            fields = info.keys()
            info = [info]
        elif isinstance(info, list):
            fields = info[0].keys()
        with open(self.file_path, mode) as myfile:
            writer = csv.DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(info)

    def edit_row(self, new_info):
        all_rows = self.read_file()
        final_rows = []
        for row in all_rows:
            if row["id"] == new_info["id"]:
                row = new_info
            final_rows.append(row)
        self.write_file(final_rows, mode="w")

    def edit_row2(self, new_info):
        all_rows = self.read_file()
        final_rows = []
        for row in all_rows:
            if row["event_name"] == new_info["event_name"]:
                row = new_info
            final_rows.append(row)
        self.write_file(final_rows, mode="w")

    def check_unique_id(self, id):
        all_rows = self.read_file()
        for row in all_rows:
            if row["id"] == str(id):
                return True
        return False

    def delete_row(self, id):
        all_rows = self.read_file()
        final_rows = []
        for row in all_rows:
            if row['national_code'] == str(id):
                continue
            final_rows.append(row)
        self.write_file(final_rows, mode="w")


# info_1 = {"id": 1, "name": "Mhdiye", "last_name": "Kaffash"}
# info_2 = {"id": 2, "name": "zahra", "last_name": "amiri"}
# my_file = FileHandler(path_file)
# # print(my_file.read_file())
# print(my_file.write_file(info_1))
# my_file.write_file(info_2)
# my_file.edit_row({"id": 1, "name": "fateme", "last_name": "fahimi"})
# print(my_file.read_file())
# my_file.delete_row(1)
# print(my_file.read_file())
