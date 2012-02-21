#!/sh/bash

target=cleaneddata

cd data
for i in `ls`
do
	cd $i
	for j in `ls`
	do
		if [ $j == NOTES ] ;then break; fi
		cp $j ../../$target/$i-`echo $j |sed -E 's/\..*|$/.txt/'`
	done
	cd ..
done
cd ..
