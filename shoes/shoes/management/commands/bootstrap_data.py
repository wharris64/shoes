from django.core.management.base import BaseCommand, CommandError
from shoes.quickstart.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help = "populates db with shoe types"

    def handle(self, *args, **options):
        colors = ["Red" 
        ,"Orange" 
        ,"Yellow" 
        ,"Green" 
        ,"Blue"
        ,"Indigo"
        ,"Violet"
        ,"White"
        ,"Black"]

        for color in colors:
            ShoeColor.objects.create(color_name=color)
        
        shoe_types =  ["sneaker",
           "boot",
           "sandal",
           "dress",
           "other"]
        for shoe_type in shoe_types:
            ShoeType.objects.create(style=shoe_type)


    # def pop_shoe_color:
    #     # something something power
