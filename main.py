import subprocess
import os
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


def archive(archive_name):
    args = ['zip', '-r', '-', '1.jpeg', '2.jpeg']
    archive_process = subprocess.Popen(args, stdout = subprocess.PIPE)
    archive_process.wait()
    archive_binary = archive_process.communicate()[0]


def write_to_file(archive_binary, archive_name):
    with open(archive_name, 'wb') as archive_file:
        archive_file.write(archive_binary)


async def archivate2(filenames_str):
    args = 'zip -r - ' + filenames_str
    archive_binary = ''
    for chunk in iter(asyncio.create_subprocess_shell(args,
                                                      stdout=asyncio.subprocess.PIPE,
                                                      limit=800)):
        print(chunk)
    print(type(archive_process))
    await asyncio.sleep(2)
    #stdout, stderr = await archive_process.communicate()
    #print('len', len(stdout))
    #archive_binary = b''
    #while True:
    #    chunk = await archive_process.stdout.read(3800)
    #    if not chunk:
    #        break
    #    archive_binary += chunk

    #write_to_file(archive_binary, 'photos_async.zip')


    #print(f'{args} exited with {archive_process.returncode}')
    #if stdout:
    #    print(f'[stdout]\n {stdout}')
    #if stderr:
    #    print(f'[stderr]\n{stderr.decode()}')


async def archivate(bash_script):
    pass


async def test(name):
    i = 0
    while i < 10:
        i += 1
        print(f'{name} - {i}')
        await asyncio.sleep(0.00001)

async def main2(loop):
    await asyncio.gather(
        test('first_func'),
        test('second_func'),
        archivate2('1.jpeg 2.jpeg 3.jpeg')
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main2(loop))
    loop.close()

