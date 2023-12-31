from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TodoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.task_input = TextInput(hint_text='Enter a task', multiline=False)
        layout.add_widget(self.task_input)
        add_button = Button(text='Add Task', on_press=self.add_task)
        layout.add_widget(add_button)
        self.task_label = TextInput(readonly=True, multiline=True)
        layout.add_widget(self.task_label)
        
        return layout

    def add_task(self, instance):
        task = self.task_input.text
        if task:
            if hasattr(self, 'tasks'):
                self.tasks.append(task)
            else:
                self.tasks = [task]
            self.task_label.text = '\n'.join(self.tasks)
            self.task_input.text = ''

if __name__ == '__main__':
    TodoApp().run()