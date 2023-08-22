# Поиск печатей

Это один из нескольких внешних модулей программы. 
Программа в целом предназначена для работы с электронными версиями документов, для ускорения осуществления перевода с одного языка на другой. 
Для этого необходмо отличать секции, на которые разделен документ, распознавать текст в них и тд.

Задача же данного модуля - поиск на документе нескольких видов штампов ( круглая синяя печать, прямоугольный штамп с текстом внутри ),
рассчет и возврат их координат, для дальнейшей обработки в основной программе. 

Модуль написан как api на фреймворке Flask и библиотеке OpenCV.

Для получения результатов необходимо отправить Post-запрос с файлом одного из форматов - .jpg, .jpeg, .png 
и указать тип документа: Свидетельство о рождении(Россия) или справка об отсутствии судимости (Россия). 
В ответе на данный запрос будут содержаться координаты обнаруженных штампов.  



## Find the Stamps

This is one of the several external program modules. 
The program as a whole is designed to work with electronic versions of documents, to accelerate the implementation of translation from one language to another. 
To do this, it is impossible to distinguish the sections into which the document is divided, to recognize the text in them, etc.

The task of this module is to search on a document of several types of stamps (round blue print, a rectangular stamp with text inside), 
calculation and return of their coordinates, for further processing in the main program.

The modul is written as API with using framework Flask and OpenCV-library
To obtain results, you need to send POST-request with a file of one of the formats - .jpg, .jpeg, .png 
and specify the type of document: Birth certificate (Russia) or a certificate of no criminal record (Russia).
The answer to this request will contain the coordinates of the detected stamps.




