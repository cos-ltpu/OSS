# Работа студента группы Б1-505 Чигажовой Ольги

Скачать данные с репозитория можно либо в графичсеком интерфейсе в zip архиве, либо склонировав.

Нужно заархивировать данные:  
`tar -cvzf git-restrict-3.0.tar.gz git-restrict`

Данные помещаются в папку SOURCES:  
`cp git-restrict-3.0.tar.gz /home/student/rpmbuild/SOURCES`

В папке SPECS описывается файл используемый для создания пакета:  
`vi git-restrict-master.spec`

Запуск создания пакета:   
`rpmbuild -ba git-restrict-master.spec`

Для подписания пакета необходимо сгенерировать ключ:  
`gpg2 --gen-key`  
При выполнении команды будет запрошено имя и email  

Экспорт открытой части ключа:  
`gpg2 --export -a 'Chigazhova Olga' > ~/rpmbuild/RPM-GPG-KEY-Chigazhova-Olga`

Создание макроса:  
`echo"%_gpg_name Chigazhova Olga">~/.rpmmacros`

Подписание пакета:  
`rpm --addsign ~/rpmbuild/RPMS/x86_64/git-restrict-3.0-1.fc32.x86_64.rpm`

