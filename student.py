from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentListButton(ListItemButton):
    pass


class Student(BoxLayout):
    first_name = ObjectProperty()
    last_name = ObjectProperty()
    student_list = ObjectProperty()

    def submit_students(self):
        student_name = self.first_name.text + ' ' + self.last_name.text
        self.student_list.adapter.data.extend([student_name])
        self.student_list._trigger_reset_populate()
        self.first_name.text = ''
        self.last_name.text = ''

    def delete_students(self):
        if self.student_list.adapter.selection:
            selection = self.student_list.adapter.selection[0].text
            self.student_list.adapter.data.remove(selection)

        self.student_list._trigger_reset_populate()

    def replace_students(self):
        if self.student_list.adapter.selection:
            selection = self.student_list.adapter.selection[0].text
            self.student_list.adapter.data.remove(selection)
            student_name = self.first_name.text + ' ' + self.last_name.text
            self.student_list.adapter.data.extend([student_name])

        self.student_list._trigger_reset_populate()


class StudentApp(App):
    def build(self):
        return Student()


stuApp = StudentApp()
stuApp.run()
