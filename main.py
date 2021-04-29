from moviepy.editor import *
import moviepy
import os 
import re # to parse this file to make the credits
import pygame
pygame.init()

PREFIX = "1080p_"
H, W = 1080, 1920 # dimensions of the final video

# These very useful functions resize the clips to
# the dimensions of the final video

VideoFileClip.reW = lambda clip :  clip.resize(width=W)
VideoFileClip.reH = lambda clip :  clip.resize(height=H)

VideoFileClip.flipX = lambda clip : moviepy.video.fx.all.mirror_x(clip)

def out(a, file="out.mp4", audio=None):
    aud = a.audio.set_fps(44100)
    a = a.without_audio().set_audio(audio or aud)
    print("output", a.w, a.h)
    a.write_videofile(PREFIX+file,
                     codec='libx264', 
                     audio_codec='aac', 
                     temp_audiofile='temp-audio.m4a', 
                     remove_temp=True,
                     threads=16)
    if file == "out.mp4":
        a.preview()
def fixsize(name):
    try:
        os.remove(PREFIX+name+"_resized.mp4")
    except FileNotFoundError:
        pass
    moviepy.video.io.ffmpeg_tools.ffmpeg_resize(PREFIX+name+".mp4", PREFIX+name+"_resized.mp4", (W,H))

# out(VideoFileClip("./clips/Clive/45 degrees 2.mp4", target_resolution=(H, W)).subclip(5.3+2.2).crop(0.1*W, 0.2*H, 0.9*W, H), "clive45.mp4")
# # fixsize("clive45")
out(VideoFileClip("./clips/Clive/45 degrees 2.mp4", target_resolution=(H, W)).subclip(5.3+2.2).crop(0.12*W, 0.24*H, 0.88*W, H), "clive45high.mp4")
fixsize("clive45high")
# out(VideoFileClip("./clips/James/IMG_9011.MOV", target_resolution=(H, W)).subclip(1.03+2.2).flipX().crop(0.15*W, 0.15*H, W, H), "james45.mp4")
# fixsize("james45")
# out(VideoFileClip("./clips/Katherine/Shot 8_1.mp4", target_resolution=(H, W)).subclip(0.1).crop(0.1*W,0.15*H,0.8*W,0.85*H), "kat45.mp4")
# fixsize("kat45")
# out(VideoFileClip("./clips/Tony/Bars 77-93 (angled).mp4", target_resolution=(H, W)).subclip(0.4+2.2).flipX().crop(0.1*W,0.05*H,W,0.95*H), "tony45.mp4")
# fixsize("tony45")
# out(VideoFileClip("./clips/Sara/Video 8.mov", target_resolution=(H, W)).subclip(0.1+2.2).margin(left=W//10).crop(0,0,0.9*W,0.9*H), "sara45.mp4")
# fixsize("sara45")
# out(VideoFileClip("./clips/Sara/Video 8.mov", target_resolution=(H, W)).subclip(0.1+2.2).crop(0,0,0.9*W,0.9*H), "sara45nomargin.mp4")
# fixsize("sara45nomargin")

clive45 = VideoFileClip(PREFIX+"clive45_resized.mp4")
clive45high = VideoFileClip(PREFIX+"clive45high_resized.mp4")
james45 = VideoFileClip(PREFIX+"james45_resized.mp4")
kat45 = VideoFileClip(PREFIX+"kat45_resized.mp4")
tony45 = VideoFileClip(PREFIX+"tony45_resized.mp4")
sara45 = VideoFileClip(PREFIX+"sara45_resized.mp4")
sara45nomargin = VideoFileClip(PREFIX+"sara45nomargin_resized.mp4")

# out(VideoFileClip("./clips/Clive/Facing camera 3.mp4", target_resolution=(H, W)).subclip(5-0.2).crop(0,0,0.9*W,0.9*H), "clive0.mp4")
# fixsize("clive0")
# out(VideoFileClip("./clips/James/IMG_9009.MOV", target_resolution=(H, W)).subclip(13.1-0.2), "james0.mp4")
# out(VideoFileClip("./clips/Katherine/Shot 7_3.mp4", target_resolution=(H, W)).subclip(0.3-0.2), "kat0.mp4")
# out(VideoFileClip("./clips/Tony/Bars 77-93 (front).mp4", target_resolution=(H, W)).subclip(3.45-0.2).crop(0,0,0.85*W,0.85*H), "tony0.mp4")
# fixsize("tony0")
# out(VideoFileClip("./clips/Tony/Bars 77-93 (front).mp4", target_resolution=(H, W)).subclip(3.45-0.2).crop(0,0.1*H,0.85*W,0.95*H), "tony0high.mp4")
# fixsize("tony0high")
# out(VideoFileClip("./clips/Sara/Video 7(1).mov", target_resolution=(H, W)).subclip(0.9-0.2), "sara0.mp4")

clive0 = VideoFileClip(PREFIX+"clive0_resized.mp4")
james0 = VideoFileClip(PREFIX+"james0.mp4")
kat0 = VideoFileClip(PREFIX+"kat0.mp4")
tony0 = VideoFileClip(PREFIX+"tony0_resized.mp4")
tony0high = VideoFileClip(PREFIX+"tony0high_resized.mp4")
sara0 = VideoFileClip(PREFIX+"sara0.mp4")

# out(VideoFileClip("./clips/Clive/VID_20210418_193046 (3).mp4", target_resolution=(H, W)).subclip(24.2, 24.2+20), "clivegrass.mp4")
# saragrass = VideoFileClip("./clips/Sara/Video 12(1).mov", target_resolution=(H, W))
# out(concatenate_videoclips([saragrass.subclip(0,1).speedx(0.5), saragrass.subclip(1)]), "saragrass.mp4")
# out(VideoFileClip("./clips/Katherine/Shot 11-12_2.mp4", target_resolution=(W, H)).rotate(90).subclip(0.4, 0.4+20), "katgrass.mp4")
# out(VideoFileClip("./clips/Tony/Bars 113-123.mp4", target_resolution=(H, W)).subclip(6.6, 6.6+20).crop(0.15*W,0.15*H,W,H), "tonygrass.mp4")
# fixsize("tonygrass")
# out(VideoFileClip("./clips/James/IMG_9019.MOV", target_resolution=(H, W)).subclip(4.95, 4.95+20), "jamesgrass.mp4")

clivegrass = VideoFileClip(PREFIX+"clivegrass.mp4")
jamesgrass = VideoFileClip(PREFIX+"jamesgrass.mp4")
katgrass = VideoFileClip(PREFIX+"katgrass.mp4")
tonygrass = VideoFileClip(PREFIX+"tonygrass_resized.mp4")
saragrass = VideoFileClip(PREFIX+"saragrass.mp4")

BORDER = 4
def layout23(clips):
    opts = {"x_center": clips[0].w/2, "width": clips[0].w*2/3}
    return CompositeVideoClip([
        clips[0].resize(0.5).margin(BORDER//2).set_position(("left","top")),
        clips[1].resize(0.5).margin(BORDER//2).set_position(("right","top")),
        clips[2].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("left","bottom")),
        clips[3].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("center","bottom")),
        clips[4].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("right","bottom")),
    ], (clips[0].w, clips[0].h))
def layout32(clips):
    opts = {"x_center": clips[0].w/2, "width": clips[0].w*2/3}
    return CompositeVideoClip([
        clips[0].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("left","top")),
        clips[1].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("center","top")),
        clips[2].crop(**opts).resize(0.5).margin(BORDER//2).set_position(("right","top")),
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
def columns(clips, widths = [0.2, 0.2, 0.2, 0.2, 0.2]):
    return CompositeVideoClip([
        clips[i].crop(x_center=clips[i].w/2, width=clips[i].w * widths[i]).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0))
        for i in range(5)
    ], (clips[0].w, clips[0].h))
def cols131(clips):
    return CompositeVideoClip([
        clips[0].crop(x_center=clips[0].w/2, width=clips[0].w/3).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[1].crop(x_center=clips[1].w/2, width=clips[1].w*2/3, height=clips[1].h*2/3).resize(0.5).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[2].crop(x_center=clips[2].w/2, width=clips[2].w*2/3, height=clips[2].h*2/3).resize(0.5).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[3].crop(x_center=clips[3].w/2, width=clips[3].w*2/3, height=clips[3].h*2/3).resize(0.5).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[4].crop(x_center=clips[4].w/2, width=clips[4].w/3).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0))
    ])
def cols131_doubled(clips):
    return CompositeVideoClip([
        clips[0].crop(x_center=clips[0].w/2, width=clips[0].w/3).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[1].crop(x_center=clips[1].w/2, width=clips[1].w/3).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[2].crop(x_center=clips[2].w/2, width=clips[2].w/3).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[3].crop(x_center=clips[3].w/2, width=clips[3].w/3).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0)),
        clips[4].crop(x_center=clips[4].w/2, width=clips[4].w/3).margin(BORDER//2).set_position((clips[i].w*sum(widths[:i]),0))
    ])

M = 240/162 # One measure

# out(concatenate_videoclips([
#     columns([katgrass, jamesgrass, tonygrass, saragrass, clivegrass]).subclip(0,5.8),
#     # columns([
#     #     concatenate_videoclips([katgrass.subclip(0,1.5), katgrass.subclip(1.5,2.5).speedx(1/1.3), katgrass.subclip(2.5)]),
#     #     jamesgrass,
#     #     concatenate_videoclips([tonygrass.subclip(0.4,2.7), tonygrass.subclip(2.7,3.7).speedx(1/.6), tonygrass.subclip(3.7)]).without_audio(),
#     #     concatenate_videoclips([saragrass.subclip(0.4,3.2), saragrass.subclip(3.2,4.2).speedx(1/.6), saragrass.subclip(4.2)]).without_audio(),
#     #     concatenate_videoclips([clivegrass.subclip(0.4,3.7), clivegrass.subclip(3.7,4.7).speedx(1/.6), clivegrass.subclip(4.7)]).without_audio()
#     # ]).subclip(0,5.8),
#     spotlight([katgrass, tonygrass, saragrass, clivegrass, jamesgrass]).subclip(5.8, 5.8+2*M),
#     spotlight([tonygrass, clivegrass, katgrass, saragrass, jamesgrass]).subclip(5.8+2*M, 5.8+4*M),
#     spotlight([clivegrass, saragrass, tonygrass, katgrass, jamesgrass]).subclip(5.8+4*M, 5.8+6*M),
#     jamesgrass.subclip(5.8+6*M)
# ]), "pt2.mp4")

ws = [0.15, 0.15, 0.4, 0.15, 0.15]
out(concatenate_videoclips([
    james0.subclip(0, 1.5),
    columns([clive45, kat45, james0, tony45.flipX(), sara45.flipX()], widths=ws).subclip(1.5, 1.5+M),
    columns([sara45, clive45, james0, kat45.flipX(), tony45.flipX()], widths=ws).subclip(1.5+M,1.5+2*M),
    columns([james45, tony45, kat0, sara45.flipX(), clive45.flipX()], widths=ws).subclip(1.5+2*M,1.5+3*M),
    columns([tony45, sara45, kat0, clive45.flipX(), james45.flipX()], widths=ws).subclip(1.5+3*M,1.5+4*M),
    columns([james45, clive45high, tony0high, sara45.flipX(), kat45.flipX()], widths=ws).subclip(1.5+4*M,1.5+5*M),
    columns([clive45high, sara45, tony0high, kat45.flipX(), james45.flipX()], widths=ws).subclip(1.5+5*M,1.5+6*M),
    columns([tony45, kat45, clive0, james45.flipX(), sara45.flipX()], widths=ws).subclip(1.5+6*M,1.5+7*M),
    columns([james45, sara45, clive0, kat45.flipX(), tony45.flipX()], widths=ws).subclip(1.5+7*M,1.5+8*M),
    columns([kat45, james45, sara0, clive45.flipX(), tony45.flipX()], widths=ws).subclip(1.5+8*M,1.5+9*M),
    columns([clive45, tony45, sara0, james45.flipX(), kat45.flipX()], widths=ws).subclip(1.5+9*M,1.5+10*M),
    layout23([kat45, james45.flipX(), tony45, sara0, clive45.flipX()]).subclip(1.5+10*M,1.5+11*M),
    layout23([clive45, kat45.flipX(), james45, tony0, sara45.flipX()]).subclip(1.5+11*M,1.5+12*M),
    layout23([sara45nomargin, clive45.flipX(), kat45, james0, tony45.flipX()]).subclip(1.5+12*M,1.5+13*M),
    layout23([tony45, sara45nomargin.flipX(), clive45, kat0, james45.flipX()]).subclip(1.5+13*M,1.5+14*M),
    layout23([kat0, james0, tony0, sara0, clive0]).subclip(1.5+14*M,28),
]), "pt1.mp4")
