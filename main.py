from moviepy.editor import *
import os 
import re # to parse this file to make the credits
import pygame
pygame.init()

H, W = 270, 480 # dimensions of the final video

# These very useful functions resize the clips to
# the dimensions of the final video

VideoFileClip.reW = lambda clip :  clip.resize(width=W)
VideoFileClip.reH = lambda clip :  clip.resize(height=H)

clive45 = VideoFileClip("./clips/Clive/45 degrees 2.mp4", target_resolution=(H, W)).subclip(5.3+2.2)
james45 = VideoFileClip("./clips/James/IMG_9011.MOV", target_resolution=(H, W)).subclip(1.03+2.2)
kat45 = VideoFileClip("./clips/Katherine/Shot 8_1.mp4", target_resolution=(H, W)).subclip(0.1)
tony45 = VideoFileClip("./clips/Tony/Bars 77-93 (angled).mp4", target_resolution=(H, W)).subclip(0.4+2.2)
sara45 = VideoFileClip("./clips/Sara/Video 8.mov", target_resolution=(H, W)).subclip(0.1+2.2)

clive0 = VideoFileClip("./clips/Clive/Facing camera 3.mp4", target_resolution=(H, W)).subclip(5-0.2)
james0 = VideoFileClip("./clips/James/IMG_9009.MOV", target_resolution=(H, W)).subclip(13.1-0.2)
kat0 = VideoFileClip("./clips/Katherine/Shot 7_3.mp4", target_resolution=(H, W)).subclip(0.3-0.2)
tony0 = VideoFileClip("./clips/Tony/Bars 77-93 (front).mp4", target_resolution=(H, W)).subclip(3.45-0.2)
sara0 = VideoFileClip("./clips/Sara/Video 7(1).mov", target_resolution=(H, W)).subclip(0.7-0.2)

# Do the laying down parts
# clive0 = VideoFileClip("./clips/Clive/Facing camera 3.mp4", target_resolution=(H, W)).subclip(5-0.2)
# james0 = VideoFileClip("./clips/James/IMG_9009.MOV", target_resolution=(H, W)).subclip(13.1-0.2)
# kat0 = VideoFileClip("./clips/Katherine/Shot 7_3.mp4", target_resolution=(H, W)).subclip(0.3-0.2)
# tony0 = VideoFileClip("./clips/Tony/Bars 77-93 (front).mp4", target_resolution=(H, W)).subclip(3.45-0.2)
# sara0 = VideoFileClip("./clips/Sara/Video 7(1).mov", target_resolution=(H, W)).subclip(0.7-0.2)

BORDER = 4
def layout23(clips):
    opts = {"x_center": clips[0].w/2, "width": clips[0].w*2/3}
    return CompositeVideoClip([
        clips[0].resize(0.5).margin(BORDER//2).set_position(("left","top")),
        clips[1].resize(0.5).margin(BORDER//2).set_position(("right","top")),
        clips[2].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("left","bottom")),
        clips[3].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("right","bottom")),
        clips[4].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("center","bottom")),
    ], (clips[0].w, clips[0].h))
def layout32(clips):
    opts = {"x_center": clips[0].w/2, "width": clips[0].w*2/3}
    return CompositeVideoClip([
        clips[0].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("left","top")),
        clips[1].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("right","top")),
        clips[2].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("center","top")),
        clips[3].resize(0.5).margin(BORDER//2).set_position(("left","bottom")),
        clips[4].resize(0.5).margin(BORDER//2).set_position(("right","bottom")),
    ], (clips[0].w, clips[0].h))
def spotlight(clips, tall=1):
    opts = {"x_center": clips[0].w/2, "width": clips[0].w*2/3}
    xpos = ["left", "center", "right"]
    return CompositeVideoClip([
        clips[0].crop(**opts).resize(0.5).margin(BORDER//2).set_position((xpos[(tall+2)%3],"top")),
        clips[1].crop(**opts).resize(0.5).margin(BORDER//2).set_position((xpos[(tall+2)%3],"bottom")),
        clips[2].crop(**opts).resize(0.5).margin(BORDER//2).set_position((xpos[(tall+1)%3],"top")),
        clips[3].crop(**opts).resize(0.5).margin(BORDER//2).set_position((xpos[(tall+1)%3],"bottom")),
        clips[4].crop(x_center=clips[0].w/2, width=clips[0].w/3).margin(BORDER//2).set_position((xpos[tall],"center")),
    ], (clips[0].w, clips[0].h))
def columns(clips):
    opts = {"x_center": clips[0].w/2, "width": clips[0].w/5}
    xpos = ["left", "center", "right"]
    return CompositeVideoClip([
        clips[0].crop(**opts).margin(BORDER//2).set_position((clips[0].w*0.0,0)),
        clips[1].crop(**opts).margin(BORDER//2).set_position((clips[0].w*0.2,0)),
        clips[2].crop(**opts).margin(BORDER//2).set_position((clips[0].w*0.4,0)),
        clips[3].crop(**opts).margin(BORDER//2).set_position((clips[0].w*0.6,0)),
        clips[4].crop(**opts).margin(BORDER//2).set_position((clips[0].w*0.8,0)),
    ], (clips[0].w, clips[0].h))


def out(a):
    aud = a.audio.set_fps(44100)
    a = a.without_audio().set_audio(aud)
    print("output", a.w, a.h)
    # a.write_videofile("out.mp4")
    a.preview()

# out(clips_array([
#     [spotlight([clive45, kat45, james45, tony45, sara45]), layout23([clive45, kat45, james45, tony45, sara45])],
#     [columns([clive45, kat45, james45, tony45, sara45]), layout32([clive45, kat45, james45, tony45, sara45])]
# ]))

out(concatenate_videoclips([
    columns([clive45, kat45, james45, tony45, sara45]).subclip(0,1),
    columns([sara45, clive45, kat45, james45, tony45]).subclip(1,2),
    columns([tony45, sara45, clive45, kat45, james45]).subclip(2,3),
    columns([james45, tony45, sara45, clive45, kat45]).subclip(3,4),
    columns([kat45, james45, tony45, sara45, clive45]).subclip(4,5),
    spotlight([clive0, james0, tony0, sara0, kat0]).subclip(5,6),
    spotlight([james0, tony0, sara0, kat0, clive0]).subclip(6,7),
    spotlight([tony0, sara0, kat0, clive0, james0]).subclip(7,8),
    spotlight([sara0, kat0, clive0, james0, tony0]).subclip(8,9),
    spotlight([kat0, clive0, james0, tony0, sara0]).subclip(9,10),
    layout23([clive45, kat45, james45, tony45, sara45]).subclip(10,11),
    layout23([sara45, clive45, kat45, james45, tony45]).subclip(11,12),
    layout23([tony45, sara45, clive45, kat45, james45]).subclip(12,13),
    layout23([james45, tony45, sara45, clive45, kat45]).subclip(13,14),
    layout23([kat45, james45, tony45, sara45, clive45]).subclip(14,15),
]))
