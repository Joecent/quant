1. when you get factors from ta-lib, you should install library TA-Lib like this:
	Download ta-lib-0.4.0-src.tar.gz and:
        untar and cd
        ./configure --prefix=/your/install/dir
        make
        sudo make install
    when install failed try to 
        export TA_INCLUDE_PATH=/your/install/dir/include
        export TA_LIBRARY_PATH=/your/install/dir/lib
2. you will install easyquant fail but you can just make from source with github addr
