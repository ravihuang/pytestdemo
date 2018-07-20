#coding:utf-8
'''
android模拟器管理
'''
import click
import subprocess
import os
import re

ANDROID_SDK = os.environ['ANDROID_HOME']
SDK_MANAGER = os.path.join(ANDROID_SDK, 'tools', 'bin', 'sdkmanager')
AVD_MANAGER = os.path.join(ANDROID_SDK, 'tools', 'bin', 'avdmanager')
EMULATOR = os.path.join(ANDROID_SDK, 'tools', 'emulator')
EMULATOR_CHECK = os.path.join(ANDROID_SDK, 'tools', 'emulator-check')
ADB = os.path.join(ANDROID_SDK, 'platform-tools', 'adb')


def call(*args):
    x=subprocess.check_output(*args,shell=True)
    print args
    #subprocess.call(*args,shell=True)
    print("------------"+x+"------------")
    return x

    
@click.group()
def cli():
    pass

@cli.command()
@click.argument('target')
@click.option('--abi', type=click.Choice(['x86', 'x86_64', 'armeabi-v7a', 'arm64-v8']), default="x86")
def install(target, abi):
    systemimg = 'system-images;%s;default;%s' % (target, abi)
    print(systemimg)
    subprocess.call([SDK_MANAGER, systemimg])

@cli.command()
@click.argument('avd')
@click.argument('target')
@click.option('--abi', type=click.Choice(['x86', 'x86_64', 'armeabi-v7a', 'arm64-v8']), default="x86")
def create(avd, target, abi):
    systemimg = 'system-images;%s;default;%s' % (target, abi)
    print(systemimg)
    call([AVD_MANAGER, 'create', 'avd', '--name', avd, '--package', systemimg])

@cli.command()
@click.argument('avd')
def delete(avd):
    call([AVD_MANAGER, 'delete', 'avd', '--name', avd])

@cli.command()
def list():
    call([AVD_MANAGER, 'list', 'avd'])

@cli.command()
@click.argument('apk')
def aapt(apk):
    '''
         return packageName and launchable-activity
    '''
    path=os.path.join(ANDROID_SDK, 'build-tools')
    dirs=os.listdir(path)
    AAPT = os.path.join(ANDROID_SDK, 'build-tools', dirs[-1], 'aapt')
    out=call([AAPT, 'dump', 'badging', apk])
    m=re.match(r"package: name='(\S*)'.*launchable-activity: name='(\S*)'",out,re.S)
    print "packageName=%s \nMain activity=%s" % (m.group(1),m.group(2))
    return m.group(1),m.group(2)
            

@cli.command()
@click.argument('avd')
def start(avd):
    '''
          启动headless模拟器
    '''
    print("Execute the following command with nohup")
    cmd = "%s -avd %s -no-audio -no-window" % (EMULATOR, avd)
    call(cmd)
@cli.command()
@click.argument('avd')
def startx(avd):
    '''
          启动模拟器
    '''    
    print("Execute the following command with nohup")
    cmd = "%s -avd %s" % (EMULATOR, avd)
    call(cmd)
    
@cli.command()
def devices():
    call([ADB, 'devices'])

# @cli.command()
# @click.argument('port')
# def stop(port):
#     '''port - every emulator listen on a local port, which can be inferred 
#        from its adb serialno, e.g., emulator-5444'''
#     with open(os.path.join(os.path.expanduser('~'), '.emulator_console_auth_token'), 'r') as f:
#         token = f.read().rstrip()
#     telnet_cmd = 'auth %s\nkill\n' % (token, )
#     call('echo "%s" | telnet 127.0.0.1 %s' % (telnet_cmd, port, ))
@cli.command()
@click.argument('device')
def stop(device=None):
    if devices:
        call([ADB,"-s",device,"emu","kill"])
    else:
        call([ADB,"emu","kill"])

@cli.command()
def check():
    call([EMULATOR_CHECK, 'accel'])


if __name__ == '__main__':
    print(u'android虚拟机管理及常用命令，设置ANDROID_HOME环境变量后使用'.encode("gbk"))
    print('Terminology:')
    print('target - something like android-19 android-23')
    print('abi - x86 x86_64 armeabi-v7a or arm64-v8')
    print('avd - an arbitrary name for an Android Virtual Device (AVD)')
    cli()