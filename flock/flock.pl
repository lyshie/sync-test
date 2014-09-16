#!/usr/bin/env perl
#===============================================================================
#
#         FILE: flock.pl
#
#        USAGE: ./flock.pl
#
#  DESCRIPTION: Only one process can enter critical session to update value
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: SHIE, Li-Yi (lyshie), lyshie@mx.nthu.edu.tw
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 2014-09-16 13:41:24
#     REVISION: ---
#===============================================================================

use strict;
use warnings;

use Time::HiRes qw(nanosleep usleep gettimeofday tv_interval);
use Fcntl qw(:DEFAULT :flock);

sub main {

    # t0
    my $t_start = [ gettimeofday() ];

    my $job_id        = $ARGV[0] || '0';
    my $sleeping_time = $ARGV[1] || '0';    # micro-second

    my $filename = '/tmp/count';

    open( FH, "+<", $filename )
      or die("ERROR: Cannot open '$filename' file.\n");

    # t1
    my $t_door = [ gettimeofday() ];
    flock( FH, LOCK_EX )
      or die("ERROR: Cannot lock '$filename' file.\n");

    # t2
    my $t_enter = [ gettimeofday() ];

    #### beginning of critical session

    # read
    my $count = 0;
    do {
        local $/ = undef;
        $count = int( <FH> || '0' );
    };
    $count++;

    # write
    seek( FH, 0, 0 );
    truncate( FH, tell(FH) );
    print FH $count;

    # show and delay
    printf( "%s => %s, ", $job_id, $count );
    usleep($sleeping_time);

    #### end of critical session

    flock( FH, LOCK_UN );

    close(FH);

    # t3
    my $t_exit = [ gettimeofday() ];

    # performance analysis
    my $t_knock     = tv_interval( $t_start, $t_door );
    my $t_lock_wait = tv_interval( $t_door,  $t_enter )
      ;    # time to wait before entering critical session

    printf( "kock time => %.7f, lock-wait time => %.7f\n",
        $t_knock, $t_lock_wait );
}

main;
