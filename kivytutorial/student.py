from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentRegistro():
    def __init__(self, fn,ln,bd,pn):
        self.first_name = fn
        self.last_name = ln
        self.birth_date = bd
        self.puppy = pn


class StudentListButton(ListItemButton):
    pass


class Student(BoxLayout):
    first_name = ObjectProperty()
    last_name = ObjectProperty()
    birth_date = ObjectProperty()
    puppy_name = ObjectProperty()
    student_list = ObjectProperty()
    students_list = []

    def submit_students(self):
        student_name = self.first_name.text + " " + self.last_name.text

        self.students_list.append(StudentRegistro(self.first_name.text,
                                                  self.last_name.text,
                                                  self.birth_date.text,
                                                  self.puppy_name.text))

        self.student_list.adapter.data.extend([student_name])
        self.student_list._trigger_reset_populate()
        self.first_name.text = ''
        self.last_name.text = ''
        print self.students_list

    def delete_students(self):
        if self.student_list.adapter.selection:
            selection = self.student_list.adapter.selection[0].text
            self.student_list.adapter.data.remove(selection)
            for i in self.students_list:
                if i.first_name in selection:
                    print "Student " + i.first_name + " Removed"
                    self.students_list.remove(i)
                    print self.students_list

        self.student_list._trigger_reset_populate()

    def replace_students(self):
        if self.student_list.adapter.selection:
            selection = self.student_list.adapter.selection[0].text
            for i in self.students_list:
                if i.first_name in selection:
                    print "Student " + i.first_name + " Removed"
                    self.students_list.remove(i)
                    print self.students_list

            self.student_list.adapter.data.remove(selection)
            student_name = self.first_name.text + ' ' + self.last_name.text
            self.student_list.adapter.data.extend([student_name])
            self.students_list.append(StudentRegistro(self.first_name.text,
                                                      self.last_name.text,
                                                      self.birth_date.text,
                                                      self.puppy_name.text))

        self.student_list._trigger_reset_populate()


class StudentApp(App):
    def build(self):
        return Student()


stuApp = StudentApp()
stuApp.run()
