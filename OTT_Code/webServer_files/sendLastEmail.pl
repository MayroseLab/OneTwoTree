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

my $subject;
my $subject_fail = "Your OneTwoTree job $id $jobTitle has failed";
my $final_status_file = "/onetwotree/results/$id/SummaryDir/FinalStatus.txt";
my $final_pass_file = "/onetwotree/results/$id/JOB_PASS.txt";

my $resultsLink = "http://onetwotree.tau.ac.il/results.html?jobId=$id";
my $message .= "Hello,\n\n";
if (-e $final_pass_file)
{
	$subject = "Your OneTwoTree results of run $id $jobTitle are ready";
	$message .= "$subject at:\n";
	$message .= "Your job was completed successfully\n";
} else {
	$subject = "Your OneTwoTree run $id $jobTitle has failed";
	$message .= "$subject_fail at:\n";
	$message .= "Please contact us for more info\n";
}


if($jobTitle)
{
	# for the url, replace spaces with %20 in $jobTitle 
	$jobTitle =~ s/ /%20/g;
	$resultsLink .= "&jobTitle=$jobTitle";
}


$message .= "$resultsLink\n\n";
$message .= "Please note: the results will be kept on the server for one month.\n\n";
$message .= "Thank you for using OneTwoTree,\n";
$message .= "OneTwoTree Team\n";

my $python_script = "/onetwotree/site/email_sender.py";

my $cmd = "python $python_script mxout.tau.ac.il $from $toEmail --subject \"$subject\" --content \"$message\":";
my $ans = `$cmd`;
if ($ans eq "ok") {
    print "Email Sent Successfully to: $toEmail\n";
}
else { 
    print "Email to $toEmail Failed\n";
}

