from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Adjust import path if sentiment_rules.py is in a subfolder
try:
    from nlp.sentiment_rules import classify_sentiment
except ImportError:
    from sentiment_rules import classify_sentiment

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="Welcome to the Feedback Sentiment Dashboard!", font_size=24))
        btn = Button(text="Go to Feedback", size_hint=(1, 0.2))
        btn.bind(on_release=self.go_to_feedback)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_to_feedback(self, instance):
        self.manager.current = 'feedback'

class FeedbackScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.layout.add_widget(Label(text="Enter your feedback:", font_size=18))
        self.input = TextInput(multiline=True, size_hint=(1, 0.5))
        self.layout.add_widget(self.input)
        self.result_label = Label(text="", font_size=16)
        self.layout.add_widget(self.result_label)
        submit_btn = Button(text="Analyze Sentiment", size_hint=(1, 0.2))
        submit_btn.bind(on_release=self.analyze_feedback)
        self.layout.add_widget(submit_btn)
        back_btn = Button(text="Back to Home", size_hint=(1, 0.2))
        back_btn.bind(on_release=self.go_to_home)
        self.layout.add_widget(back_btn)
        self.add_widget(self.layout)

    def analyze_feedback(self, instance):
        feedback = self.input.text
        sentiment = classify_sentiment(feedback)
        self.result_label.text = f"Sentiment: {sentiment.capitalize()}"

    def go_to_home(self, instance):
        self.manager.current = 'home'

class FeedbackSentimentApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(FeedbackScreen(name='feedback'))
        return sm

if __name__ == '__main__':
    FeedbackSentimentApp().run()