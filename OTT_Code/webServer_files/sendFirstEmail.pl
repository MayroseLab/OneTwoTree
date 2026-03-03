use strict;
use warnings;

use Getopt::Long;

my $jobTitle;
my $toEmail;
my $id;

GetOptions(
	"jobTitle=s"        => \$jobTitle,
	"toEmail=s"        => \$toEmail,
	"id=s"     => \$id
);

my $from = 'evolseq@tauex.tau.ac.il';

my $subject = "Your OneTwoTree job $id $jobTitle is being processed.";

my $resultsLink = "http://onetwotree.tau.ac.il/results.html?jobId=$id";
if($jobTitle)
{
	# for the url, replace spaces with %20 in $jobTitle 
	$jobTitle =~ s/ /%20/g;
	$resultsLink .= "&jobTitle=$jobTitle";
}

my $message .= "Hello,\n\n".$subject. "\nA link to your job is available at:\n";
$message .= "$resultsLink\n\n";

$message .= "We will email you again when processing is finished.\n\n";
$message .= "Thank you for using OneTwoTree\n";

my $python_script = "/onetwotree/site/email_sender.py";

my $cmd = "python $python_script mxout.tau.ac.il $from $toEmail --subject \"$subject\" --content \"$message\":";
my $ans = `$cmd`;
if ($ans eq "ok") {
    print "Email Sent Successfully to: $toEmail\n";
}
else { 
    print "Email to $toEmail Failed\n";
}
