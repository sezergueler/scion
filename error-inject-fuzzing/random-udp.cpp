
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <iostream>
#include <crafter.h>

/* Collapse namespaces */
using namespace std;
using namespace Crafter;

void launch_random_packet( string src_ip, string dst_ip, int src_port, int dst_port ) {
  /* Set the interface */
  string iface = "eth0";

  /* Create an IP header */
  IP ip_header;
  /* Set the Source and Destination IP address */
  ip_header.SetSourceIP( src_ip );
  ip_header.SetDestinationIP( dst_ip );

  /* Create a UDP header */
  UDP udp_header;
  udp_header.SetSrcPort( src_port );
  udp_header.SetDstPort( dst_port );

  /* A raw layer, this could be any array of bytes or chars */
  int payload_len = rand() % 512;
  int i;
  byte payload_bytes[payload_len];
  for (i = 0; i < payload_len; i++ ) {
    payload_bytes[i] = (byte) rand();
  }
  RawLayer payload( payload_bytes, payload_len );

  /* Create a packets */
  Packet udp_packet = ip_header / udp_header / payload;

  // cout << src_ip << ":" << src_port << " -> " << dst_ip << ":" << dst_port << ", len = " << payload_len << endl;

  /* Write the packet on the wire */
  udp_packet.Send();
}

int main() {
  string ip_net = "127.0.0.";
  int start_ip = 1;
  int end_ip = 255;
  string node_ips[ end_ip - start_ip + 1 ];
  int i;
  char tmp_str[32];

  for (i=start_ip; i<=end_ip; i++ ) {
    sprintf( tmp_str, "%d", i );
    node_ips[i-start_ip] = ip_net + tmp_str;
  }

#define NUM_PORTS 7
  short_word ports[NUM_PORTS] = {30040, 50000, 30053, 58133, 35990, 45297, 41265};
  time_t randseed = time( NULL );

  cout << "Random seed: " << randseed << endl;
  srand( randseed );

  for (i=0; i<100000; i++) {
    int j=rand() % (end_ip - start_ip + 1);
    int k=rand() % (end_ip - start_ip + 1);
    int l=rand() % NUM_PORTS;
    int m=rand() % NUM_PORTS;

    launch_random_packet( node_ips[j], node_ips[k], ports[l], ports[m] );
  }

  return 0;
}
