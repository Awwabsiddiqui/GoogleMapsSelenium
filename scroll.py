import time


def scroll(self, content):
    for i in range(6, 25, 3):
        last_review = content
        self.execute_script('arguments[0].scrollIntoView(true);', last_review)
        time.sleep(2)
