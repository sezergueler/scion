
The Libcrafter library was used for this packet injection: https://code.google.com/p/libcrafter/
Please follow the installation instructions at the above web page, you will also need these libraries:
sudo apt-get install libpcap0.8 libpcap0.8-dev
sudo apt-get install autoconf libtool

You can adjust the IP address space you want to use for source and destination addresses:
  string ip_net = "127.0.0.";
  int start_ip = 1;
  int end_ip = 255;

Same for port numbers, right now it uses:
#define NUM_PORTS 7
  short_word ports[NUM_PORTS] = {30040, 50000, 30053, 58133, 35990, 45297, 41265};

make

then launch with:> sudo ./random-udp

Enjoy!
