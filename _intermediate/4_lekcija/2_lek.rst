
..
  Пермутације, варијације, комбинације
  reading

==========================
 Пермутације и комбинације
==========================



Пермутације
-----------

Дефиниција пермутације гласи:
k-пермутација од n објеката је сваки уређен избор k објеката од њих n колико их је на располагању.
Односно за сваку од таквих пермутација кажемо, укратко, да је k пермутација од n.
n пермутација од n је просто пермутација од n елемената.
Нпр 2-пермутација од 4 (овде узимамо да је основни скуп (a,b,c,d)) је заправо:

ab,ac,ad,bc,bd,cd,ba,ca,da,cb,db,dc.

k-пермутација од n још се и називају варијацијама без понављања k-те класе од n елемената.

Број пермутација
----------------

Број k пермутација од n различитих објеката означићемо са :math:`P(n,k)`.
Како бисмо доказали следећу теорему:
:math:`P(n,k)=n(n-1)...(n-k+1)`.

**Доказ:**


Пошто има n различитих објеката, први члан k пермутације може се изабрати на n начина.
Пошто је он изабран остаје још n-1 објекат за избор на друго место у пермутацији.
Трећи се може изабрати на n-2 начина, и тако даље са осталим члановима.
Док последњи k-ти члан може бити изабран на n-(k-1) што је једнако n-k+1 начин.
На основу овога закључујемо да је укупан број начина за образовање једне k пермутације производ n(n-1)...(n-k+1), чиме је доказана теорема.

Комбинације
-----------

k-комбинација од n је сваки неуређен избор било којих k елемената од љих n колико 
их је на располагању.
Ако објекти чине скуп (a,b,c,d), онда су 2-комбинације ab и ba идентичне 
јер редослед није од важности.
Тако да од ова 4 објекта (a,b,c,d) имамо шест скупова 2-комбинација:
ab,ac,ad,bc,bd,cd.

Број комбинација
----------------


Број k комбинација од n различитих објеката добија се доказивањем следеће теореме.
Теорема. Број свих k комбинација од n различитих објеката, који ћемо означити са :math:`C(n,k)` је: 
Теорема се доказује решавањем биномног коефицијента.

**Доказ:**

Свака  k комбинација од n различитих објеката може се уредити на  k! 
различитих начина, и при сваком од тих уређења добија се по једна  k 
комбинација од n различитих објеката. 
Ако означимо број тих комбинација са :math:`C(n,k)`, 
из овога што је речено и из обрасца за број свих k комбинација од n различитих објеката следи: 

.. figure:: ../../_images/ккомбинација.png
   :width: 450px   
   :align: center






**Примери**


**Пример 1.**

Између 10 особа треба изабрати комисију од 4 члана.
На колико начина тај избор може бити учињен ако постоје две посвађане особе 
које не могу бити заједно у комисији?

*Решење 1.*

Ако изузмемо посвађане особе, постоји још 8 кандидата за комисију, па избор може бити обављен на 
:math:`C(8,4)=70` начина, не рачунајући комисију чији члан један од посвађаних особа.
Поред обог броја могуће је образовати комисију чији је члан један од предходно изузетих.
На основу принципа производа и обрасца за број комбинација, таквих комисија може бити :math:`2C(8,3)=112`, 
јер сваку од посвађаних особа можемо придружити већ изабраном трочланом одбору и тако добити 
избор од 4 члана.Из принципа збира следи да је укупан број могућих комисија 70+112=182.

**Пример 2.**

Између седам мушкараца и четири жене треба изабрати групу од шест особа.
На колико се начина то може извести ако је у групи обавезно да буду најмање две жене?

*Решење 2.*

Могу се изабрати две три или четири жене.Две жене је могуће изабрати на :math:`C(4,2)` 
што је једнако 6 начина.После тога треба изабрати 4 мушкарца за шта постоји :math:`C(7,4)=35` начина.
Према правилу производа две жене и четири мушкарца могу се изабрати на :math:`C(4,2)C(7,4)=210` 
начина.За избор три жене и три мушкарца могућих начина има :math:`C(4,3)C(7,3)=140`.
На крају за избор четири жене и два мушкарца 
:math:`C(4,4)C(7,2)=21`.
Према принципу збира укупан број начина да се тражене особе изаберу износи 210+140+21=371.

Задаци за самосталан рад
------------------------


**Задатак 1.**

Колико различитих четвороцифрених бројева можемо написати помоћу следећих цифара (0,1,2,3,4,5,6), узимајући у обзир да се свака од цифара може понављати? 


**Задатак 2.**

У једној установи запослено је 1000 особа.Да ли је могуће да све оне имају различите иницијале?

