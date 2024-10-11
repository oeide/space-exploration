#!/usr/bin/perl
if ($#ARGV != 0)
{
    print "˜´\n\nUse: generateMapSet.pl <parameterList.txt>\n\n";
}
else
{
    $paramList= $ARGV[0];
    print "Parameter list: " . $paramList . "\n";
    print "\n";
    print "\n";
    $scriptRoot= "~/Documents/GitHub/space-exploration/scripts/";
    
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
