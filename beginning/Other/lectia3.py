In [1]: 1/0                                                                                                             
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-1-9e1622b385b6> in <module>
----> 1 1/0

ZeroDivisionError: division by zero

In [2]: raise Exception('uau!!!')                                                                                       
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-2-781ec0f0d63e> in <module>
----> 1 raise Exception('uau!!!')

Exception: uau!!!

In [3]: try: 
   ...:     1/0 
   ...:     print('a mers!') 
   ...: except: 
   ...:     print('a crapat!') 
   ...:      
   ...:                                                                                                                 
a crapat!

In [4]: a = 1                                                                                                           

In [5]: b = 1.                                                                                                          

In [6]: type(a)                                                                                                         
Out[6]: int

In [7]: type(b)                                                                                                         
Out[7]: float

In [8]: type(a) == int                                                                                                  
Out[8]: True

In [9]: type(b) == int                                                                                                  
Out[9]: False

In [10]: TypeError                                                                                                      
Out[10]: TypeError

In [11]: type(TypeError)                                                                                                
Out[11]: type

In [12]: dir(TypeError)                                                                                                 
Out[12]: 
['__cause__',
 '__class__',
 '__context__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__suppress_context__',
 '__traceback__',
 'args',
 'with_traceback']

In [13]: l = [1,2,3]                                                                                                    

In [14]: it = iter(l)                                                                                                   

In [15]: next(it)                                                                                                       
Out[15]: 1

In [16]: next(it)                                                                                                       
Out[16]: 2

In [17]: next(it)                                                                                                       
Out[17]: 3

In [18]: next(it)                                                                                                       
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-18-bc1ab118995a> in <module>
----> 1 next(it)

StopIteration: 

In [19]: it = iter(l)                                                                                                   

In [20]: while next(it): 
    ...:     pass 
    ...:                                                                                                                
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-20-56d9fb7e74ea> in <module>
----> 1 while next(it):
      2     pass
      3 

StopIteration: 

In [21]: print('a=', end=''); print('123')                                                                              
a=123

In [22]: old_print = print                                                                                              

In [23]:                                                                                                                

In [23]:                                                                                                                

In [23]: old_print('cucu bau')                                                                                          
cucu bau

In [24]: def new_print(*args): 
    ...:     old_print(*args) 
    ...:                                                                                                                

In [25]: def new_print(*args): 
    ...:     args = [ 'NEW:'+str(x) for x in args ] 
    ...:     old_print(*args) 
    ...:                                                                                                                

In [26]: print = new_print                                                                                              

In [27]:                                                                                                                

In [27]:                                                                                                                

In [27]:                                                                                                                

In [27]: print(1)                                                                                                       
NEW:1

In [28]: print(1,2,3,)                                                                                                  
NEW:1 NEW:2 NEW:3

In [29]: print(1,2,3,'aaa')                                                                                             
NEW:1 NEW:2 NEW:3 NEW:aaa

In [30]: old_print(1,2,3,'aaa')                                                                                         
1 2 3 aaa

In [31]: [sum, min, max]                                                                                                
Out[31]: [<function sum(iterable, start=0, /)>, <function min>, <function max>]

In [32]: fns = [sum, min, max]                                                                                          

In [33]: x = [1,2,3]                                                                                                    

In [34]:                                                                                                                

In [34]: [ f(x) for f in fns ]                                                                                          
Out[34]: [6, 1, 3]

In [35]: def greeting(mesaj): 
    ...:     def greet(x): 
    ...:         print(mesaj, x) 
    ...:     return greet 
    ...:                                                                                                                

In [36]:                                                                                                                

In [36]: greeting('hei')                                                                                                
Out[36]: <function __main__.greeting.<locals>.greet(x)>

In [37]: g1 = greeting('hei')                                                                                           

In [38]: g1('horia')                                                                                                    
NEW:hei NEW:horia

In [39]: g2 = greeting('bai! ')                                                                                         

In [40]: g2('horia')                                                                                                    
NEW:bai!  NEW:horia

In [41]: class Persoana: 
    ...:     def __init__(nume, prenume): 
    ...:         self.nume = nume 
    ...:         self.prenume = prenume 
    ...:                                                                                                                

In [42]:                                                                                                                

In [42]: p = Persoana('horia', 'cristescu')                                                                             
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-2985eb86ee71> in <module>
----> 1 p = Persoana('horia', 'cristescu')

TypeError: __init__() takes 2 positional arguments but 3 were given

In [43]: class Persoana: 
    ...:     def __init__(self, nume, prenume): 
    ...:         self.nume = nume 
    ...:         self.prenume = prenume 
    ...:                                                                                                                

In [44]: p = Persoana('horia', 'cristescu')                                                                             

In [45]: p                                                                                                              
Out[45]: <__main__.Persoana at 0x107da9e50>

In [46]: p.nume                                                                                                         
Out[46]: 'horia'

In [47]: p.prenume                                                                                                      
Out[47]: 'cristescu'

In [48]: class Persoana: 
    ...:     def __init__(self, nume, prenume): 
    ...:         self.nume = nume 
    ...:         self.prenume = prenume 
    ...:      
    ...:     def greet(self): 
    ...:         print('Salut', self.nume, self.prenume) 
    ...:                                                                                                                

In [49]:                                                                                                                

In [49]: type(p)                                                                                                        
Out[49]: __main__.Persoana

In [50]: __main__.Persoana                                                                                              
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-50-738164cd700d> in <module>
----> 1 __main__.Persoana

NameError: name '__main__' is not defined

In [51]: Persoana                                                                                                       
Out[51]: __main__.Persoana

In [52]: p = Persoana('horia', 'cristescu')                                                                             

In [53]: p.greet()                                                                                                      
NEW:Salut NEW:horia NEW:cristescu

In [54]: print = old_print                                                                                              

In [55]: p.greet()                                                                                                      
Salut horia cristescu

In [56]: p.nume                                                                                                         
Out[56]: 'horia'

In [57]: p.prenume                                                                                                      
Out[57]: 'cristescu'

In [58]: p.greet                                                                                                        
Out[58]: <bound method Persoana.greet of <__main__.Persoana object at 0x107cf2e10>>

In [59]: p.greet()                                                                                                      
Salut horia cristescu

In [60]: p2 = Persoana('Diana', 'Cristescu')                                                                            

In [61]:                                                                                                                

In [61]: id(p)                                                                                                          
Out[61]: 4425985552

In [62]: id(p2)                                                                                                         
Out[62]: 4426733776

In [63]: p.nume                                                                                                         
Out[63]: 'horia'

In [64]: p2.nume                                                                                                        
Out[64]: 'Diana'

In [65]: p.greet()                                                                                                      
Salut horia cristescu

In [66]: p2.greet()                                                                                                     
Salut Diana Cristescu

In [67]:                                                                                                                

In [67]:                                                                                                                

In [67]:                                                                                                                

In [67]: p3 = { 'nume': 'Cristescu', 'prenume': 'Balu' }                                                                

In [68]: def greet(p): 
    ...:     print('Salut', p['nume'], p['prenume']) 
    ...:                                                                                                                

In [69]:                                                                                                                

In [69]: greet(p3)                                                                                                      
Salut Cristescu Balu

In [70]: p3['greet']=greet                                                                                              

In [71]: p3                                                                                                             
Out[71]: {'nume': 'Cristescu', 'prenume': 'Balu', 'greet': <function __main__.greet(p)>}

In [72]: p3['greet'](p3)                                                                                                
Salut Cristescu Balu

In [73]:                                                                                                                                                              

In [73]:                                                                                                                                                              

In [73]:                                                                                                                                                              

In [73]:                                                                                                                                                              

In [73]:                                                                                                                                                              

In [73]: import os                                                                                                                                                    

In [74]: dir os                                                                                                                                                       
  File "<ipython-input-74-9be48194569a>", line 1
    dir os
         ^
SyntaxError: invalid syntax


In [75]: dir(os)                                                                                                                                                      
Out[75]: 
['CLD_CONTINUED',
 'CLD_DUMPED',
 'CLD_EXITED',
 'CLD_TRAPPED',
 'DirEntry',
 'EX_CANTCREAT',
 'EX_CONFIG',
 'EX_DATAERR',
 'EX_IOERR',
 'EX_NOHOST',
 'EX_NOINPUT',
 'EX_NOPERM',
 'EX_NOUSER',
 'EX_OK',
 'EX_OSERR',
 'EX_OSFILE',
 'EX_PROTOCOL',
 'EX_SOFTWARE',
 'EX_TEMPFAIL',
 'EX_UNAVAILABLE',
 'EX_USAGE',
 'F_LOCK',
 'F_OK',
 'F_TEST',
 'F_TLOCK',
 'F_ULOCK',
 'MutableMapping',
 'NGROUPS_MAX',
 'O_ACCMODE',
 'O_APPEND',
 'O_ASYNC',
 'O_CLOEXEC',
 'O_CREAT',
 'O_DIRECTORY',
 'O_DSYNC',
 'O_EXCL',
 'O_EXLOCK',
 'O_NDELAY',
 'O_NOCTTY',
 'O_NOFOLLOW',
 'O_NONBLOCK',
 'O_RDONLY',
 'O_RDWR',
 'O_SHLOCK',
 'O_SYNC',
 'O_TRUNC',
 'O_WRONLY',
 'PRIO_PGRP',
 'PRIO_PROCESS',
 'PRIO_USER',
 'P_ALL',
 'P_NOWAIT',
 'P_NOWAITO',
 'P_PGID',
 'P_PID',
 'P_WAIT',
 'PathLike',
 'RTLD_GLOBAL',
 'RTLD_LAZY',
 'RTLD_LOCAL',
 'RTLD_NODELETE',
 'RTLD_NOLOAD',
 'RTLD_NOW',
 'R_OK',
 'SCHED_FIFO',
 'SCHED_OTHER',
 'SCHED_RR',
 'SEEK_CUR',
 'SEEK_END',
 'SEEK_SET',
 'ST_NOSUID',
 'ST_RDONLY',
 'TMP_MAX',
 'WCONTINUED',
 'WCOREDUMP',
 'WEXITED',
 'WEXITSTATUS',
 'WIFCONTINUED',
 'WIFEXITED',
 'WIFSIGNALED',
 'WIFSTOPPED',
 'WNOHANG',
 'WNOWAIT',
 'WSTOPPED',
 'WSTOPSIG',
 'WTERMSIG',
 'WUNTRACED',
 'W_OK',
 'X_OK',
 '_Environ',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_execvpe',
 '_exists',
 '_exit',
 '_fspath',
 '_get_exports_list',
 '_putenv',
 '_spawnvef',
 '_unsetenv',
 '_wrap_close',
 'abc',
 'abort',
 'access',
 'altsep',
 'chdir',
 'chflags',
 'chmod',
 'chown',
 'chroot',
 'close',
 'closerange',
 'confstr',
 'confstr_names',
 'cpu_count',
 'ctermid',
 'curdir',
 'defpath',
 'device_encoding',
 'devnull',
 'dup',
 'dup2',
 'environ',
 'environb',
 'error',
 'execl',
 'execle',
 'execlp',
 'execlpe',
 'execv',
 'execve',
 'execvp',
 'execvpe',
 'extsep',
 'fchdir',
 'fchmod',
 'fchown',
 'fdopen',
 'fork',
 'forkpty',
 'fpathconf',
 'fsdecode',
 'fsencode',
 'fspath',
 'fstat',
 'fstatvfs',
 'fsync',
 'ftruncate',
 'get_blocking',
 'get_exec_path',
 'get_inheritable',
 'get_terminal_size',
 'getcwd',
 'getcwdb',
 'getegid',
 'getenv',
 'getenvb',
 'geteuid',
 'getgid',
 'getgrouplist',
 'getgroups',
 'getloadavg',
 'getlogin',
 'getpgid',
 'getpgrp',
 'getpid',
 'getppid',
 'getpriority',
 'getsid',
 'getuid',
 'initgroups',
 'isatty',
 'kill',
 'killpg',
 'lchflags',
 'lchmod',
 'lchown',
 'linesep',
 'link',
 'listdir',
 'lockf',
 'lseek',
 'lstat',
 'major',
 'makedev',
 'makedirs',
 'minor',
 'mkdir',
 'mkfifo',
 'mknod',
 'name',
 'nice',
 'open',
 'openpty',
 'pardir',
 'path',
 'pathconf',
 'pathconf_names',
 'pathsep',
 'pipe',
 'popen',
 'pread',
 'putenv',
 'pwrite',
 'read',
 'readlink',
 'readv',
 'register_at_fork',
 'remove',
 'removedirs',
 'rename',
 'renames',
 'replace',
 'rmdir',
 'scandir',
 'sched_get_priority_max',
 'sched_get_priority_min',
 'sched_yield',
 'sendfile',
 'sep',
 'set_blocking',
 'set_inheritable',
 'setegid',
 'seteuid',
 'setgid',
 'setgroups',
 'setpgid',
 'setpgrp',
 'setpriority',
 'setregid',
 'setreuid',
 'setsid',
 'setuid',
 'spawnl',
 'spawnle',
 'spawnlp',
 'spawnlpe',
 'spawnv',
 'spawnve',
 'spawnvp',
 'spawnvpe',
 'st',
 'stat',
 'stat_result',
 'statvfs',
 'statvfs_result',
 'strerror',
 'supports_bytes_environ',
 'supports_dir_fd',
 'supports_effective_ids',
 'supports_fd',
 'supports_follow_symlinks',
 'symlink',
 'sync',
 'sys',
 'sysconf',
 'sysconf_names',
 'system',
 'tcgetpgrp',
 'tcsetpgrp',
 'terminal_size',
 'times',
 'times_result',
 'truncate',
 'ttyname',
 'umask',
 'uname',
 'uname_result',
 'unlink',
 'unsetenv',
 'urandom',
 'utime',
 'wait',
 'wait3',
 'wait4',
 'waitpid',
 'walk',
 'write',
 'writev']

In [76]:                                                                                                                                                              

In [76]:                                                                                                                                                              

In [76]: import os                                                                                                                                                    

In [77]: os.open                                                                                                                                                      
Out[77]: <function posix.open(path, flags, mode=511, *, dir_fd=None)>

In [78]: open                                                                                                                                                         
Out[78]: <function io.open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)>

In [79]: dir(os.path)                                                                                                                                                 
Out[79]: 
['__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_get_sep',
 '_joinrealpath',
 '_varprog',
 '_varprogb',
 'abspath',
 'altsep',
 'basename',
 'commonpath',
 'commonprefix',
 'curdir',
 'defpath',
 'devnull',
 'dirname',
 'exists',
 'expanduser',
 'expandvars',
 'extsep',
 'genericpath',
 'getatime',
 'getctime',
 'getmtime',
 'getsize',
 'isabs',
 'isdir',
 'isfile',
 'islink',
 'ismount',
 'join',
 'lexists',
 'normcase',
 'normpath',
 'os',
 'pardir',
 'pathsep',
 'realpath',
 'relpath',
 'samefile',
 'sameopenfile',
 'samestat',
 'sep',
 'split',
 'splitdrive',
 'splitext',
 'stat',
 'supports_unicode_filenames',
 'sys']

In [80]: !pwd                                                                                                                                                         
/Users/diana

In [81]: !ls -la                                                                                                                                                      
total 128
drwxrwxrwx+ 36 diana  staff   1224 Dec 21 11:45 .
drwxr-xr-x   7 diana  staff    238 May  5  2019 ..
-r--------   1 diana  staff      7 Mar  3  2016 .CFUserTextEncoding
-rw-r--r--@  1 diana  staff  14340 Nov 16 16:31 .DS_Store
drwx------   4 diana  staff    136 Dec 19 17:39 .Trash
-rw-------   1 diana  staff      0 Jul 19  2018 .Xauthority
drwxr-xr-x   5 diana  staff    170 Sep 29  2018 .android
-rw-r--r--   1 diana  staff  25618 Dec 21 09:49 .bash_history
-rw-r--r--   1 diana  staff    168 Aug 12 01:29 .bash_profile
drwxr-xr-x  36 diana  staff   1224 Dec 21 11:45 .bash_sessions
drwxr-xr-x   3 diana  staff    102 May 29  2019 .cache
drwxr-xr-x   5 diana  staff    170 Jun 27 01:18 .config
drwx------   3 diana  staff    102 May 25  2016 .cups
drwxr-xr-x   5 diana  staff    170 Nov  9 11:04 .ipython
-rw-------   1 diana  staff    204 Nov  9 10:55 .joe_state
drwxr-xr-x  11 diana  staff    374 Jan 12  2017 .litwrl
drwxr-xr-x   3 diana  staff    102 Jul  4  2016 .local
drwxr-xr-x   3 diana  staff    102 Jun 27 02:33 .mono
drwxr-xr-x   6 diana  staff    204 Jul  5 23:04 .oracle_jre_usage
-rw-------   1 diana  staff     13 Nov  9 11:03 .python_history
-rw-------   1 diana  staff   1024 Jul 19  2018 .rnd
drwxr-xr-x   4 diana  staff    136 Dec 21 00:30 .vscode
drwxrwxrwx   8 diana  staff    272 Jun 27 02:31 Applications
drwxr-xr-x   9 diana  staff    306 May 22  2019 Calibre Library
drwxrwxr-x@  4 diana  staff    136 Sep  7  2017 Creative Cloud Files
drwx------+  8 diana  staff    272 Dec  8 00:53 Desktop
drwx------+ 14 diana  staff    476 Dec  3 06:48 Documents
drwx------+ 26 diana  staff    884 Dec  3 06:53 Downloads
drwx------@ 85 diana  staff   2890 Dec 21 10:30 Library
drwxr-xr-x   2 diana  staff     68 Feb 25  2018 MacKeeper Backups
drwx------+  4 diana  staff    136 Jun 26 21:52 Movies
drwx------+  7 diana  staff    238 Jan 27  2018 Music
drwx------+  5 diana  staff    170 Jul 25  2018 Pictures
drwxr-xrwx+  5 diana  staff    170 Mar  3  2016 Public
drwxr-xr-x   3 diana  staff    102 Jul 23 01:40 Twitch
drwxr-xr-x   3 diana  staff    102 Jul  4  2016 VirtualBox VMs

In [82]: os.path.join('/Users/diana', 'Music')                                                                                                                        
Out[82]: '/Users/diana/Music'

In [83]: os.path.join('/Users/diana/', 'Music')                                                                                                                       
Out[83]: '/Users/diana/Music'

In [84]: os.path.join('/Users/diana/', '/Music')                                                                                                                      
Out[84]: '/Music'

In [85]: os.path.join('/Users/diana/', './Music')                                                                                                                     
Out[85]: '/Users/diana/./Music'

In [86]: os.path.join('/Users/diana/', 'Music')                                                                                                                       
Out[86]: '/Users/diana/Music'

In [87]: '/Users/diana/' + 'Music'                                                                                                                                    
Out[87]: '/Users/diana/Music'

In [88]: os.getcwd()                                                                                                                                                  
Out[88]: '/Users/diana'

In [89]: import glob                                                                                                                                                  

In [90]: glob.glob('*.txt')                                                                                                                                           
Out[90]: []

In [91]: !ls -la                                                                                                                                                      
total 128
drwxrwxrwx+ 36 diana  staff   1224 Dec 21 11:45 .
drwxr-xr-x   7 diana  staff    238 May  5  2019 ..
-r--------   1 diana  staff      7 Mar  3  2016 .CFUserTextEncoding
-rw-r--r--@  1 diana  staff  14340 Nov 16 16:31 .DS_Store
drwx------   4 diana  staff    136 Dec 19 17:39 .Trash
-rw-------   1 diana  staff      0 Jul 19  2018 .Xauthority
drwxr-xr-x   5 diana  staff    170 Sep 29  2018 .android
-rw-r--r--   1 diana  staff  25618 Dec 21 09:49 .bash_history
-rw-r--r--   1 diana  staff    168 Aug 12 01:29 .bash_profile
drwxr-xr-x  36 diana  staff   1224 Dec 21 11:45 .bash_sessions
drwxr-xr-x   3 diana  staff    102 May 29  2019 .cache
drwxr-xr-x   5 diana  staff    170 Jun 27 01:18 .config
drwx------   3 diana  staff    102 May 25  2016 .cups
drwxr-xr-x   5 diana  staff    170 Nov  9 11:04 .ipython
-rw-------   1 diana  staff    204 Nov  9 10:55 .joe_state
drwxr-xr-x  11 diana  staff    374 Jan 12  2017 .litwrl
drwxr-xr-x   3 diana  staff    102 Jul  4  2016 .local
drwxr-xr-x   3 diana  staff    102 Jun 27 02:33 .mono
drwxr-xr-x   6 diana  staff    204 Jul  5 23:04 .oracle_jre_usage
-rw-------   1 diana  staff     13 Nov  9 11:03 .python_history
-rw-------   1 diana  staff   1024 Jul 19  2018 .rnd
drwxr-xr-x   4 diana  staff    136 Dec 21 00:30 .vscode
drwxrwxrwx   8 diana  staff    272 Jun 27 02:31 Applications
drwxr-xr-x   9 diana  staff    306 May 22  2019 Calibre Library
drwxrwxr-x@  4 diana  staff    136 Sep  7  2017 Creative Cloud Files
drwx------+  8 diana  staff    272 Dec  8 00:53 Desktop
drwx------+ 14 diana  staff    476 Dec  3 06:48 Documents
drwx------+ 26 diana  staff    884 Dec  3 06:53 Downloads
drwx------@ 85 diana  staff   2890 Dec 21 10:30 Library
drwxr-xr-x   2 diana  staff     68 Feb 25  2018 MacKeeper Backups
drwx------+  4 diana  staff    136 Jun 26 21:52 Movies
drwx------+  7 diana  staff    238 Jan 27  2018 Music
drwx------+  5 diana  staff    170 Jul 25  2018 Pictures
drwxr-xrwx+  5 diana  staff    170 Mar  3  2016 Public
drwxr-xr-x   3 diana  staff    102 Jul 23 01:40 Twitch
drwxr-xr-x   3 diana  staff    102 Jul  4  2016 VirtualBox VMs

In [92]: glob.glob('Desktop/*.txt')                                                                                                                                   
Out[92]: []

In [93]: glob.glob('Desktop/*')                                                                                                                                       
Out[93]: 
['Desktop/\\',
 'Desktop/Books',
 'Desktop/Poze Bunicu',
 'Desktop/Python',
 'Desktop/Variante Bac 2009.odt']

In [94]: glob.glob('Desktop/*.odt')                                                                                                                                   
Out[94]: ['Desktop/Variante Bac 2009.odt']

In [95]: import glob                                                                                                                                                  

In [96]: for name in glob.glob('*'): 
    ...:     if os.path.isfile(name): 
    ...:         print('Fisier', name) 
    ...:     else: 
    ...:         print('Director', name) 
    ...:                                                                                                                                                              
Director Applications
Director Calibre Library
Director Creative Cloud Files
Director Desktop
Director Documents
Director Downloads
Director Library
Director MacKeeper Backups
Director Movies
Director Music
Director Pictures
Director Public
Director Twitch
Director VirtualBox VMs

In [97]: for name in glob.glob('Desktop/*'): 
    ...:     if os.path.isfile(name): 
    ...:         print('Fisier', name) 
    ...:     else: 
    ...:         print('Director', name) 
    ...:                                                                                                                                                              
Director Desktop/\
Director Desktop/Books
Director Desktop/Poze Bunicu
Director Desktop/Python
Fisier Desktop/Variante Bac 2009.odt

In [98]: for name in glob.glob('*.txt'): 
    ...:     if os.path.isfile(name): 
    ...:         print('Fisier', name) 
    ...:     else: 
    ...:         print('Director', name) 
    ...:                                                                                                                                                              
Fisier diana.txt

In [99]: with open('diana.txt', 'r') as f: 
    ...:     for line in f: 
    ...:         print(line) 
    ...:                                                                                                                                                              
abc

def

ijk




In [100]: with open('diana.txt', 'r') as f: 
     ...:     for line in f: 
     ...:         print(line, end='') 
     ...:          
     ...:                                                                                                                                                             
abc
def
ijk


In [101]: i = 0 
     ...: with open('diana.txt', 'r') as f: 
     ...:     for line in f: 
     ...:         i += 1 
     ...:         print(i, line, end='') 
     ...:          
     ...:                                                                                                                                                             
1 abc
2 def
3 ijk
4 

In [102]: i = 0 
     ...: with open('diana.txt', 'r') as f: 
     ...:     print(list(f)) 
     ...:      
     ...:          
     ...:                                                                                                                                                             
['abc\n', 'def\n', 'ijk\n', '\n']

In [103]: import                                                                                                                                                      
  File "<ipython-input-103-d76e22c112c9>", line 1
    import
          ^
SyntaxError: invalid syntax


In [104]: import os                                                                                                                                                   

In [105]: type(os.path)                                                                                                                                               
Out[105]: module

In [106]: def fn(x): 
     ...:     return x*2 
     ...:                                                                                                                                                             

In [107]:                                                                                                                                                             

In [107]: fn(5)                                                                                                                                                       
Out[107]: 10

In [108]: fn.cucu = 5                                                                                                                                                 

In [109]: fn(5)                                                                                                                                                       
Out[109]: 10

In [110]: fn.cucu                                                                                                                                                     
Out[110]: 5

