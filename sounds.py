import os
from pygame import mixer

mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
soundtrack = mixer.music.load('data/soundtrack/Ugh.wav')
mixer.music.set_volume(0.2)


def load_sound(name):
    fullname = os.path.join('data', name)
    sound = mixer.Sound(fullname)
    return sound


detecting = load_sound('soundtrack/detecting.ogg')
detecting.set_volume(0.3)
doors = load_sound('soundtrack/doors.ogg')
doors.set_volume(1)
pistol_machinegun = load_sound('soundtrack/pistol_machinegun.ogg')
pistol_machinegun.set_volume(0.3)
sniper_shot = load_sound('soundtrack/pistol_machinegun.ogg')
sniper_shot.set_volume(0.2)
rat_shot = load_sound('soundtrack/shotgun.ogg')
rat_shot.set_volume(0.2)
steps = load_sound('soundtrack/steps.ogg')
steps.set_volume(1)
click = load_sound('soundtrack/click.ogg')
click.set_volume(0.2)
shotgun = load_sound('soundtrack/shotgun.ogg')
shotgun.set_volume(1)
robo_dying = load_sound('soundtrack/robo_dying.ogg')
robo_dying.set_volume(0.3)
splash = load_sound('soundtrack/splash.ogg')
splash.set_volume(0.6)
pick_up = load_sound('soundtrack/pick_up.ogg')
pick_up.set_volume(0.6)
pick_up2 = load_sound('soundtrack/pick_up2.ogg')
pick_up2.set_volume(5)
strike = load_sound('soundtrack/strike.ogg')
strike.set_volume(0.4)
hit = load_sound('soundtrack/hit.ogg')
hit.set_volume(0.1)
dying = load_sound('soundtrack/dying.ogg')
dying.set_volume(0.6)
reload = load_sound('soundtrack/reload.ogg')
reload.set_volume(0.6)
blink = load_sound('soundtrack/blink.ogg')
blink.set_volume(0.3)
punch = load_sound('soundtrack/punch.ogg')
punch.set_volume(1.5)
thrill = load_sound('soundtrack/thrill.ogg')
thrill.set_volume(0.7)