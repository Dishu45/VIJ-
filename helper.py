import logging   #Bot Created by 𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import subprocess   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import datetime   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import asyncio   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import os   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import requests   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import time   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
from p_bar import progress_bar   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import aiohttp   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import aiofiles   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import tgcrypto   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import concurrent.futures   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
import subprocess   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
from pyrogram.types import Message   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
from pyrogram import Client, filters   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
def duration(filename):   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                             "format=duration", "-of",   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                             "default=noprint_wrappers=1:nokey=1", filename],   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        stdout=subprocess.PIPE,   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        stderr=subprocess.STDOUT)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    return float(result.stdout)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
       #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
def exec(cmd):   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        process = subprocess.run(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        output = process.stdout.decode()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        print(output)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        return output   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        #err = process.stdout.decode()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
def pull_run(work, cmds):   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        print("Waiting for tasks to complete")   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        fut = executor.map(exec,cmds)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
async def aio(url,name):   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    k = f'{name}.pdf'   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    async with aiohttp.ClientSession() as session:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        async with session.get(url) as resp:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            if resp.status == 200:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                f = await aiofiles.open(k, mode='wb')   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                await f.write(await resp.read())   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                await f.close()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    return k   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
async def download(url,name):   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    ka = f'{name}.pdf'   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    async with aiohttp.ClientSession() as session:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        async with session.get(url) as resp:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            if resp.status == 200:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                f = await aiofiles.open(ka, mode='wb')   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                await f.write(await resp.read())   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                await f.close()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    return ka   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
def parse_vid_info(info):   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    info = info.strip()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    info = info.split("\n")   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    new_info = []   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    temp = []   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    for i in info:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        i = str(i)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        if "[" not in i and '---' not in i:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            while "  " in i:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                i = i.replace("  ", " ")   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            i.strip()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            i = i.split("|")[0].split(" ",2)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            try:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                if "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                    temp.append(i[2])   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                    new_info.append((i[0], i[2]))   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            except:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                pass   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    return new_info   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
def vid_info(info):   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    info = info.strip()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    info = info.split("\n")   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    new_info = dict()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
    temp = []   #Bot Created by @NtrRazYt
    for i in info:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        i = str(i)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
        if "[" not in i and '---' not in i:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            while "  " in i:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                i = i.replace("  ", " ")   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            i.strip()   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            i = i.split("|")[0].split(" ",3)   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
            try:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                if "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                    temp.append(i[2])   #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                       #Bot Created by @𝕃𝕦𝕔𝕚𝕗𝕖𝕣
                    # temp.update(f'{i[2]}')   #Bot Created by @NtrRazYt
                    # new_info.append((i[2], i[0]))   #Bot Created by @NtrRazYt
                    #  mp4,mkv etc ==== f"({i[1]})"    #Bot Created by @NtrRazYt
                       #Bot Created by @NtrRazYt
                    new_info.update({f'{i[2]}':f'{i[0]}'})   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
            except:   #Bot Created by @NtrRazYt
                pass   #Bot Created by @NtrRazYt
    return new_info   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
async def run(cmd):   #Bot Created by @NtrRazYt
    proc = await asyncio.create_subprocess_shell(   #Bot Created by @NtrRazYt
        cmd,   #Bot Created by @NtrRazYt
        stdout=asyncio.subprocess.PIPE,   #Bot Created by @NtrRazYt
        stderr=asyncio.subprocess.PIPE)   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
    stdout, stderr = await proc.communicate()   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
    print(f'[{cmd!r} exited with {proc.returncode}]')   #Bot Created by @NtrRazYt
    if proc.returncode == 1:   #Bot Created by @NtrRazYt
        return False   #Bot Created by @NtrRazYt
    if stdout:   #Bot Created by @NtrRazYt
        return f'[stdout]\n{stdout.decode()}'   #Bot Created by @NtrRazYt
    if stderr:   #Bot Created by @NtrRazYt
        return f'[stderr]\n{stderr.decode()}'   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
       #Bot Created by @NtrRazYt
       #Bot Created by @NtrRazYt
       #Bot Created by @NtrRazYt
def old_download(url, file_name, chunk_size = 1024 * 10):   #Bot Created by @NtrRazYt
    if os.path.exists(file_name):   #Bot Created by @NtrRazYt
        os.remove(file_name)   #Bot Created by @NtrRazYt
    r = requests.get(url, allow_redirects=True, stream=True)   #Bot Created by @NtrRazYt
    with open(file_name, 'wb') as fd:   #Bot Created by @NtrRazYt
        for chunk in r.iter_content(chunk_size=chunk_size):   #Bot Created by @NtrRazYt
            if chunk:   #Bot Created by @NtrRazYt
                fd.write(chunk)   #Bot Created by @NtrRazYt
    return file_name   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
def human_readable_size(size, decimal_places=2):   #Bot Created by @NtrRazYt
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:   #Bot Created by @NtrRazYt
        if size < 1024.0 or unit == 'PB':   #Bot Created by @NtrRazYt
            break   #Bot Created by @NtrRazYt
        size /= 1024.0   #Bot Created by @NtrRazYt
    return f"{size:.{decimal_places}f} {unit}"   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
def time_name():   #Bot Created by @NtrRazYt
    date = datetime.date.today()   #Bot Created by @NtrRazYt
    now = datetime.datetime.now()   #Bot Created by @NtrRazYt
    current_time = now.strftime("%H%M%S")   #Bot Created by @NtrRazYt
    return f"{date} {current_time}.mp4"   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
async def download_video(url,cmd, name):   #Bot Created by @NtrRazYt
    download_cmd = f'{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args "aria2c: -x 16 -j 32"'   #Bot Created by @NtrRazYt
    global failed_counter   #Bot Created by @NtrRazYt
    print(download_cmd)   #Bot Created by @NtrRazYt
    logging.info(download_cmd)   #Bot Created by @NtrRazYt
    k = subprocess.run(download_cmd, shell=True)   #Bot Created by @NtrRazYt
    if "visionias" in cmd and k.returncode != 0 and failed_counter <= 10:   #Bot Created by @NtrRazYt
        failed_counter += 1   #Bot Created by @NtrRazYt
        await asyncio.sleep(5)   #Bot Created by @NtrRazYt
        await download_video(url, cmd, name)   #Bot Created by @NtrRazYt
    failed_counter = 0   #Bot Created by @NtrRazYt
    try:   #Bot Created by @NtrRazYt
        if os.path.isfile(name):   #Bot Created by @NtrRazYt
            return name   #Bot Created by @NtrRazYt
        elif os.path.isfile(f"{name}.webm"):   #Bot Created by @NtrRazYt
            return f"{name}.webm"   #Bot Created by @NtrRazYt
        name = name.split(".")[0]   #Bot Created by @NtrRazYt
        if os.path.isfile(f"{name}.mkv"):   #Bot Created by @NtrRazYt
            return f"{name}.mkv"   #Bot Created by @NtrRazYt
        elif os.path.isfile(f"{name}.mp4"):   #Bot Created by @NtrRazYt
            return f"{name}.mp4"   #Bot Created by @NtrRazYt
        elif os.path.isfile(f"{name}.mp4.webm"):   #Bot Created by @NtrRazYt
            return f"{name}.mp4.webm"   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
        return name   #Bot Created by @NtrRazYt
    except FileNotFoundError as exc:   #Bot Created by @NtrRazYt
        return os.path.isfile.splitext[0] + "." + "mp4"   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
async def send_doc(bot: Client, m: Message,cc,ka,cc1,prog,count,name):   #Bot Created by @NtrRazYt
    reply = await m.reply_text(f"Uploading - `{name}`")   #Bot Created by @NtrRazYt
    time.sleep(1)   #Bot Created by @NtrRazYt
    start_time = time.time()   #Bot Created by @NtrRazYt
    await m.reply_document(ka,caption=cc1)   #Bot Created by @NtrRazYt
    count+=1   #Bot Created by @NtrRazYt
    await reply.delete (True)   #Bot Created by @NtrRazYt
    time.sleep(1)   #Bot Created by @NtrRazYt
    os.remove(ka)   #Bot Created by @NtrRazYt
    time.sleep(3)    #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
async def send_vid(bot: Client, m: Message,cc,filename,thumb,name,prog):   #Bot Created by @NtrRazYt
       #Bot Created by @NtrRazYt
    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)   #Bot Created by @NtrRazYt
    await prog.delete (True)   #Bot Created by @NtrRazYt
    reply = await m.reply_text(f"**Uploading ...** - `{name}`")   #Bot Created by @NtrRazYt
    try:   #Bot Created by @NtrRazYt
        if thumb == "no":   #Bot Created by @NtrRazYt
            thumbnail = f"{filename}.jpg"   #Bot Created by @NtrRazYt
        else:   #Bot Created by @NtrRazYt
            thumbnail = thumb   #Bot Created by @NtrRazYt
    except Exception as e:   #Bot Created by @NtrRazYt
        await m.reply_text(str(e))   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
    dur = int(duration(filename))   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
    start_time = time.time()   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
    try:   #Bot Created by @NtrRazYt
        await m.reply_video(filename,caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))   #Bot Created by @NtrRazYt
    except Exception:   #Bot Created by @NtrRazYt
        await m.reply_document(filename,caption=cc, progress=progress_bar,progress_args=(reply,start_time))   #Bot Created by @NtrRazYt
    os.remove(filename)   #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
    os.remove(f"{filename}.jpg")   #Bot Created by @NtrRazYt
    await reply.delete (True)   #Bot Created by @NtrRazYt
       #Bot Created by @NtrRazYt
   #Bot Created by @NtrRazYt
