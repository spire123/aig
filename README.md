# lab2

### Amazon EC2
https://erp.metbhujbalknowledgecity.ac.in/StudyMaterial/01AG042022010780007.pdf


### Cloud Computing (Google App Engine)
Deploy app engine: https://cloud.google.com/build/docs/deploying-builds/deploy-appengine
https://drive.google.com/file/d/1hhKOG5yvCKBLJceCg5S-WVEC7m84M9oy/view?usp=share_link


### Cloud Computing (Apex Programming)
site: https://studyber.com/creating-an-application-in-salesforce-com-using-apex-programming-language/
https://drive.google.com/file/d/1PeU--jnQktiUp0AMb3WZYWywFYLlJCJs/view?usp=share_link

code 1 :
```
public class mayur {
    public static void create(String Name, String Phone){
        account ac = new account();
        ac.Name = Name;
        ac.Phone = Phone;
        insert ac;
        System.debug('Account Created Successful for '+ ac.name);
    }
}
```

code 2:

```
public class firstClass1 {
 public static void Addition()
{
 Integer a = 4;
 Integer b = 5;
 Integer c = a + b;
 Integer d = 4 + 5;
 Integer e = a + 5;
 System.debug('Add = ' + c);
 System.debug('Add =' + d);
 System.debug('Add =' + e);
}
 public static void Subtraction()
 {
   Integer a = 4;
   Integer b = 5;
   Integer c1 = a - b;
   Integer d1 = b - a;
   Integer e1 = 4 - 5;
   Integer f1 = a - 5;
   System.debug('Sub ='+ c1);
   System.debug('Sub =' + d1);
   System.debug('Sub =' + e1);
   System.debug('Sub =' + f1);
 }
 public static void Multi()
 {
    Integer a = 4;
    Integer b = 5;
    Integer c = a * b;
    Integer d = 4 * 5;
    Integer e = a * 5;
    System.debug(c);
    System.debug(d);
    System.debug(e);
    Integer f = -4;
    Integer g = a * f;
    System.debug(g);
 }
 public static void Div()
 {
    Integer a = 4;
    Integer b = 5;
    Integer c = a / b;
    Integer d = 4 / 5;
    Integer e = a / 5;
    System.debug(c);
    System.debug(d);
    System.debug(e);
 }
}
```


### Cloud Computing (Custom Application)
https://studyber.com/design-and-develop-custom-application-mini-project-using-sales-force-cloud/

https://drive.google.com/file/d/1D1m-y1UmoRzp-npeKMdyxSxZgulxGc3I/view?usp=share_link

***Steps:***
1) custome obj
2) Tabs
3) App manager -> new lightning app
4) user profile -> system admin
5) go to 9 dots search app name

