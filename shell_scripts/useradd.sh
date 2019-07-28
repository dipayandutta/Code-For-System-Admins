if [ $(id -u) -eq 0 ];then

	for user in `more users.txt`
	do
	echo $user
	useradd	-g MCA -m -p $user -s /bin/bash $user
	echo $user:$user | chpasswd
	done
else
	echo "Only root user can add users!"
	exit 2
fi
