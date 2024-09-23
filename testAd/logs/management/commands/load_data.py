from django.core.management.base import BaseCommand
from logs.models import LogEvent
from faker import Faker


ELEMENTS = (
    'load',
    'resize',
    'scroll',
    'error',
    'click',
    'dblclick',
    'mousedown',
    'mouseup',
    'mousemove',
    'mouseenter',
    'mouseleave',
    'mouseover',
    'mouseout',
    'contextmenu',
    'keydown',
    'keyup',
    'keypress',
    'input',
    'change',
    'focus',
    'blur',
    'submit',
    'reset',
    'touchstart',
    'touchend',
    'touchmove',
    'play',
    'pause',
    'ended',
    'online',
    'offline',
    'dragstart',
    'drag',
    'dragend',
    'dragenter',
    'dragleave',
    'dragover',
    'drop',
)


class Command(BaseCommand):
    help = 'Load fake log events'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Create 10 fake events
            hostname = fake.hostname()
            date = fake.date_time_this_year().strftime("%Y-%m-%d_%H-%M-%S")
            LogEvent.objects.create(
                timestamp= date,
                computer_name=hostname,
                event_type=fake.random_element(elements=ELEMENTS),
                application=fake.word(),
                window_title=fake.catch_phrase(),
                content=fake.text(max_nb_chars=50),
                screenshot_url=f"logs/screenshots/{hostname}_LogEvent_{date}.jpg"
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded fake data'))
