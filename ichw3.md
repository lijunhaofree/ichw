高速缓冲储存器是存在于CPU和主存之间的一级存储器，由静态存储芯片（SRAM)组成，容量比较小但速度比主存快得多。其功能就是用来存放那些近期需要运行的指令和数据，以提高CPU对储存器的访问速度。

工作原理：

首先，要清楚电脑里CPU的速度最快，然后是内存，最后是硬盘。如果CPU要从硬盘里读取数据，CPU只能等硬盘将读取的数据一点一点的放到内存，在进行处理。由于CPU处理速度太快，硬盘读取数据的速度远远跟不上CPU处理的速度。这样CPU大部分的时间是在等待数据，而不是在处理数据。会造成很大的CPU资源浪费。当加入告诉缓存后，硬盘可以将数据读出现放入缓存，等到一定的量后，在放入内存让CPU处理。CPU在处理这批数据时，硬盘有可以用这段时间读取新的数据到缓存。若CPU处理完这次的数据，可是硬盘还没将缓存的数据放入内存。CPU可以去执行别的任务，不用等待数据。高速的缓存就相当于一个中转仓库

1.CPU 访问 Cache

2.若有数据, 则命中, 转4; 否则转3

3.到内存中复制需要的数据块, 覆盖 Cache 的内容

4.CPU 存取 Cache


