import kivy_grade_calc

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class GradeCalc(BoxLayout):
    grade_input = ''

    def backspace_button(self, text_input):
        self.display.text = text_input[:-1]

    def calculate_button(self, text_input):
        # TODO: add handling for accidental space press
        try:
            grade_percentage = kivy_grade_calc.grade_converter(float(text_input.strip()))
            self.result.text = str(grade_percentage)
            self.display.text = ''
        except ValueError:
            pass

    def space_button(self, text_input):
        if self.display.text == '':
            pass
        else:
            try:
                list_of_grades = kivy_grade_calc.make_list(text_input)
                grade = kivy_grade_calc.check_range(list_of_grades[-1])
                if isinstance(grade, str):
                    self.result.text = grade

                self.display.text = f'{text_input}, '
            except ValueError:
                pass

    def avg_button(self, text_input):
        try:
            list_of_grades = kivy_grade_calc.make_list(text_input)
            grade_average = kivy_grade_calc.find_average(list_of_grades)

            self.display.text = str(grade_average)
        except ValueError:
            pass


class GradeCalcApp(App):
    def build(self):
        app = GradeCalc()

        return app


if __name__ == '__main__':
    GradeCalcApp().run()