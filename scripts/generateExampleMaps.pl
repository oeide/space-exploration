#!/usr/bin/perl
$komm0= "python ./reearchPlan.py";
print "\n";
print $komm0;
print "\n";
print "\n";
system("$komm0");

if ($#ARGV != 0)
{
    print "˜´\n\nUse: generateExampleMaps.pl <rootFolder>\n\n";
}
else
{
    $rot= $ARGV[0];
    print "Root folder: " . $rot . "\n";
    print "\n";
    print "\n";
    $scriptRoot= "~/Documents/GitHub/space-exploration/scripts/";
    readthis($rot, $scriptRoot);
}

sub readthis
{
    my $path = @_[0];
    my $scriptsPath = @_[1];
    #print "Path: " . $path;
    #print "\n";
    opendir FILEDIR, $path;
    my @files = sort grep !/^\.\.?$/,readdir FILEDIR;
    foreach $name (@files)
    {
        my $path2 = $path.'/'.$name;
        if(-d $path2)
        {
            readthis($path2, $scriptRoot);
        }
        else
        {
            if ($name =~ /(\.csv)$/)
            {
                process_file($path2, $scriptRoot);
            }
        }
    }
}

sub process_file{
    my $csvfile = @_[0];
    my $scriptsRoot = @_[1];
    $komm1= "python " . $scriptRoot . "callMapGeneration.py " . $csvfile;
    print $komm1;
    print "\n";
    print "\n";
    system("$komm1");
}
