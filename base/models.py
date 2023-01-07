from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    BISON = 'Bison'
    WOLF = 'Wolf'
    ELK = 'Elk'
    BLACKBEAR = 'Black Bear'
    GRIZZLY = 'Grizzly Bear'
    MOOSE = 'Moose'
    MOUNTAINLION = 'Mountain Lion'
    COYOTE = 'Coyote'
    PRONGHORN = 'Pronghorn'
    BIGHORNSHEEP = 'Bighorn Sheep'
    BALDEAGLE = 'Bald Eagle'
    BOBCAT = 'Bobcat'
    REDFOX = 'Red Fox'
    TRUMPETERSWAN = 'Trumpeter Swan'
    YELLOWBELLIEDMARMOT = 'Yellow-bellied Marmot'
    RIVEROTTER = 'River Otter'
    LYNX = 'Lynx'
    SHREW = 'Shrew'
    PIKA = 'Pika'
    SQUIRREL = 'Squirrel'
    MULEDEER = 'Mule Deer'
    SANDHILLCRANE = 'Sandhill Crane'
    FLYINGSQUIRREL = 'Flying Squirrel'
    UINTAGROUNDSQUIRREL = 'Uinta Ground Squirrel'
    MONTANEVOLE = 'Montane Vole'
    EASTERNMEADOWVOLE = 'Eastern Meadow Vole'
    BUSHYTAILEDWOODRAT = 'Bushy-tailed Woodrat'
    CHIPMUNK = 'Chipmunk'
    UINTACHIPMUNK = 'Uinta Chipmunk'
    WHITETAILEDJACKRABBIT = 'White-tailed Jackrabbit'
    BEAVER = 'Beaver'
    AMERICANMARTEN = 'American Marten'
    MOUNTAINCHICKADEE = 'Mountain Chickadee'
    BOREALCHORUSFROG = 'Boreal Chorus Frog'
    CUTTHROATTROUT = 'Cutthroat Trout'
    GREATHORNEDOWL = 'Great Horned Owl'
    SNOWSHOEHARE = 'Snowshoe Hare'
    ROCKYMOUNTAINELK = 'Rocky Mountain Elk'
    NORTHWESTERNWOLF = 'Northwestern Wolf'
    BLACKFOOTEDFERRET = 'Black-footed Ferret'
    WOLVERINE = 'Wolverine'
    ANIMALS = [
        (BISON, ('Bison')),
        (WOLF, ('Wolf')),
        (ELK, ('Elk')),
        (BLACKBEAR, ('Black Bear')),
        (GRIZZLY, ('Grizzly Bear')),
        (MOOSE, ('Moose')),
        (MOUNTAINLION, ('Mountain Lion')),
        (COYOTE, ('Coyote')),
        (PRONGHORN, ('Pronghorn')),
        (BIGHORNSHEEP, ('Bighorn Sheep')),
        (BALDEAGLE, ('Bald Eagle')),
        (BOBCAT, ('Bobcat')),
        (REDFOX, ('Red Fox')),
        (TRUMPETERSWAN, ('Trumpeter Swan')),
        (YELLOWBELLIEDMARMOT, ('Yellow-bellied Marmot')),
        (RIVEROTTER, ('River Otter')),
        (LYNX, ('Lynx')),
        (SHREW, ('Shrew')),
        (PIKA, ('Pika')),
        (SQUIRREL, ('Squirrel')),
        (MULEDEER, ('Mule Deer')),
        (SANDHILLCRANE, ('Sandhill Crane')),
        (FLYINGSQUIRREL, ('Flying Squirrel')),
        (UINTAGROUNDSQUIRREL, ('Uinta Ground Squirrel')),
        (MONTANEVOLE, ('Montane Vole')),
        (EASTERNMEADOWVOLE, ('Eastern Meadow Vole')),
        (BUSHYTAILEDWOODRAT, ('Bushy-tailed Woodrat')),
        (CHIPMUNK, ('Chipmunk')),
        (UINTACHIPMUNK, ('Uinta Chipmunk')),
        (WHITETAILEDJACKRABBIT, ('White-tailed Jackrabbit')),
        (BEAVER, ('Beaver')),
        (AMERICANMARTEN, ('American Marten')),
        (MOUNTAINCHICKADEE, ('Mountain Chickadee')),
        (BOREALCHORUSFROG, ('Boreal Chorus Frog')),
        (CUTTHROATTROUT, ('Cutthroat Trout')),
        (GREATHORNEDOWL, ('Great Horned Owl')),
        (SNOWSHOEHARE, ('Snowshoe Hare')),
        (ROCKYMOUNTAINELK, ('Rocky Mountain Elk')),
        (NORTHWESTERNWOLF, ('Northwestern Wolf')),
        (BLACKFOOTEDFERRET, ('Black-footed Ferret')),
        (WOLVERINE, ('Wolverine'))
    ]

    animal = models.CharField(max_length=32, choices=ANIMALS, default=BISON)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.animal

