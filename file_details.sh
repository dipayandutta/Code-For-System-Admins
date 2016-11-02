
#Author:-Dipayan Dutta

#USE:- programm to count number of indivual files 
      #and also total files , work as ls | wc -l 
      #with indivual file counter . 

#Usage :- #just move this file in the directory 
	 #change the permission to execute mode
	 #chmod a+x file_details.sh
	 #And run it 
	 #./file_details.sh 

#version : - 0.1 (More Mdification will be uploaded)

#NOTE : - This program is also a good example of case and for loop 



#!/bin/bash


c_count=0
txt_count=0
sh_count=0
java_count=0
cpp_count=0
py_count=0
doc_count=0
pdf_count=0
html_count=0
css_count=0
js_count=0
php_count=0

for file in $(ls)
do 
	ext=${file#*\.}
	case $ext in
	c)
	c_count=`expr $c_count + 1`;
	;;
	txt)
	txt_count=`expr $txt_count + 1`;
	;;
	sh)
	sh_count=`expr $sh_count + 1`;
	;;
	java)
	java_count=`expr $java_count + 1`;
	;;
	cpp)
	cpp_count=`expr $cpp_count + 1`;
	;;
	py)
	py_count=`expr $py_count + 1`;
	;;
	doc)
	doc_count=`expr $doc_count + 1`;
	;;
	docx)
	doc_count=`expr $doc_count + 1`;
	;;
	pdf)
	pdf_count=`expr $pdf_count + 1`;
	;;
	html)
	html_count=`expr $html_count + 1`;
	;;
	css)
	css_count=`expr $css_cout + 1`;
	;;
	js)
	js_count=`expr $js_count + 1`;
	;;
	php)
	php_count=`expr $php_count + 1`;
	;;
	*) 
	file_with_out_extension=`expr $file_with_out_extension + 1`;
	;;
	esac
done

echo "Current Directory `pwd`"
echo "==========================="
echo "Here is the file Details"
echo "==========================="
echo "Total C file ==> "$c_count;
echo "Total sh file ==> "$sh_count;
echo "Total text file ==>"$txt_count;
echo "Total java file ==>"$java_count;
echo "Total cpp file ==>" $cpp_count;
echo "Total python file ==>"$py_count;
echo "Total Document file ==>"$doc_count;
echo "Total pdf file ==>"$pdf_count;
echo "Total html file ==>"$html_count;
echo "Total css file ==>"$css_count;
echo "Total js file ==>"$js_count;
echo "Total php file ==>"$php_count;
echo "File with out Extension ==>"$file_with_out_extension;

total_files=$(( $c_count + $sh_count + $txt_count + $java_count + $cpp_count +$py_count + $doc_count + $pdf_count + $file_with_out_extension + $html_count + $css_count + $js_count + $php_count));

echo "total Number of files in the diretory == >"$total_files;
