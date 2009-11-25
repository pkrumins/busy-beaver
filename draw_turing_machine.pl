#!/usr/bin/perl
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# Turing Machine tape drawer.
# More info at: http://www.catonmat.net/blog/busy-beaver
#
# Version 1.1
#

use warnings;
use strict;
use GD;

$|++;

my $input_file = shift or die 'Usage: $0 <file with TM state transitions>';
my $cell_size = shift || 4;
my $im_file = "$input_file.png";

sub line_count { 
    my $count = 0;
    open my $fh, '<', shift or die $!;
    $count += tr/\n/\n/ while sysread($fh, $_, 2**20);
    return $count;
}

sub get_last_line {
    my $file = shift;
    my $last_line = `tail -1 $file`;
    chomp $last_line;
    return $last_line;
}

my $nr_lines = line_count $input_file;
my $last_line = get_last_line $input_file;
my $last_width = length($last_line);

my ($width, $height) = ($cell_size*$last_width, $cell_size*$nr_lines);

my $im = GD::Image->new($width, $height);
my $white = $im->colorAllocate(255,255,255);
my $dark = $im->colorAllocate(40, 40, 40);

my ($x, $y) = (0, $height-$cell_size);

print "Starting to draw the image. Total states: $nr_lines.\n";
print "It will be $width x $height pizels in size.\n";

my $prev_line;
my ($pad_left, $pad_right) = (0, 0);

sub pad {
    my ($line, $left, $right) = @_;
    return '0'x$left . $line . '0'x$right;
}

open my $fh, "-|", "/usr/bin/tac $input_file" or die $!;
while (<$fh>) {
    chomp;
    print "." if $. % 10 == 0;
    print "($.)" if $. % 500 == 0;

    $prev_line = $_ unless defined $prev_line;

    my $new_line;
    if (length $_ != length $prev_line) {
        if ($prev_line =~ /0$/) {
            $pad_right++;
        }
        elsif ($prev_line =~ /^0/) {
            $pad_left++;
        }
        else {
            die "unexpected data at $. in file $input_file";
        }
    }
    $new_line = pad($_, $pad_left, $pad_right);
    $prev_line = $_;

    my @cells = split //, $new_line;
    for my $cell (@cells) {
        $im->filledRectangle($x, $y, $x + $cell_size, $y + $cell_size,
                $cell ? $dark : $white);
        $x += $cell_size;
    }
    $y -= $cell_size;
    $x = 0;

}

print "\n";

{
    open my $fh, ">", $im_file or die $!;
    print $fh $im->png;
    close $fh;
}

print "Done. Image saved to $im_file.\n";

