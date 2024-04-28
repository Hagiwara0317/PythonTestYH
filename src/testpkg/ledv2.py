from time import sleep
import RPi.GPIO as GPIO
#インポート

def freeLed(n,x,y):#nは出力するpin,xは何回出力するか,yは何秒間隔で出力するか
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(n,GPIO.OUT)#出力するpinを設定
      sleep(2)#そのままだと最初の出力が画面の切り替わりで見えないから遅延入れた
      num = 0
      while num < x:#出力回数
             GPIO.output(n,GPIO.HIGH)
             sleep(y)#sleepで何秒出力するか設定
             GPIO.output(n,GPIO.LOW)
             sleep(y)#同様にsleepで何秒待つか設定
             num += 1
             #ここまで来たら繰り返し

if __name__ == '__main__':#通常のプログラムとして実行された時用
    freeLed()
