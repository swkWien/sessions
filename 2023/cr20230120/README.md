# Zero Overhead Coderetreat 20. Jan. 2023  

Bring Your Own Topic  

## Schedule  

08:45 - 09:00 Welcome  
09:00 - 09:15 Check-in  
09:15 - 09:30 Topics  

_Recall coding dojo mindset and rules of engagement._

## Check-in  

*   Gregor: tired, excited  
    
*   Adam: early, let's take Friday off  
    
*   Serhii: no sleep  
    
*   Peter: full of plans for today  
    
*   Rea: Worried, because WLAN isn't working, and I can't participate on phone data. Hopeful that it will soon be back up again. Looking forward to today  
    
*   Eike: Will join a bit later. fine  
    

## Topics  

*   usw kata Langton's Ant for a change (Peter/Rea)  
    *   [http://en.wikipedia.org/wiki/Langton%27s\_ant](http://en.wikipedia.org/wiki/Langton%27s_ant)  
        
    *   also this kata was recommended on some pathway to learn TDD  
        
*   Constraint TDD Evil Pair mit Property based testing (Peter)
    *   [list of PBT tools](https://gist.github.com/npryce/4147916), for Java use [jquik](https://jqwik.net/)  
        
    *   The question is if PBT has a stronger effect on driving code, as it uses random values (something people want to do when doing Evil Pair)  
        
*   Constraint LoD on purely functional code (Peter)  
    *   [https://www.ccs.neu.edu/home/lieber/LoD.html](https://www.ccs.neu.edu/home/lieber/LoD.html) and [famous paper](https://www2.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/paper-boy/demeter.pdf)  
        
    *   Does it make sense? Does it even apply to FP code?  
        
    *   Some strong FP would be great, Haskell anyone?  
        
    *   [Fantasy Battle](https://github.com/Neppord/FantasyBattle-Refactoring-Kata) has PureScript  
        
    *   maybe "Lenses" have something to do with it  
        *   [https://github.com/gcanti/monocle-ts](https://github.com/gcanti/monocle-ts)  
            
        *   [https://www.fpcomplete.com/haskell/tutorial/lens/](https://www.fpcomplete.com/haskell/tutorial/lens/)  
            
        *   [https://arrow-kt.io/docs/optics/](https://arrow-kt.io/docs/optics/)  
            
*   Talk about how we want to proceed with invitations when SWK mail isn't working (Rea)  
    
*   Complete Game of Life (Eike)  
    

If we do an ensemble, we are explicit about responsibilities.  

## Session 1: Law of Demeter for Functional Code  

kata - [Fantasy Battle](https://github.com/Neppord/FantasyBattle-Refactoring-Kata) in PureScript  
repository - [https://github.com/gregorriegler/FantasyBattle-Refactoring-Kata  
](https://github.com/gregorriegler/FantasyBattle-Refactoring-Kata)gitpod.io - [https://gregorriegl-fantasybatt-uf7wzgucpud.ws-eu83.gitpod.io/  
](https://gregorriegl-fantasybatt-uf7wzgucpud.ws-eu83.gitpod.io/)timer - [https://mobti.me/swkretreat](https://mobti.me/swkretreat)  

0930-1015 What is going on here -- 1015 Break  
1025-1115 Test -- 1115 Break  
1125-1215 Extract method to Equipment -- 1215 Lunch  
1310-1410 Extract 2nd method, try to make it generic  
1410 Closing  

LoD: Who knows what? We could think about dots? Modules?  
"Each unit should have only limited knowledge about other units: only units "closely" related to the current unit."  

[https://harry.garrood.me/blog/write-your-own-generics/](https://harry.garrood.me/blog/write-your-own-generics/)  

## Final Retro  

_What did we do and learn?_  

(R) learned about FP and purescript - how to define functions etc. - not quite sure yet which parts are purescript syntax, and what is FP more generally.  

(S) experienced mob programming approach  
(S) LoD considerations  
(S) recap/re-dive into FP  

(G) purescript a bit  
(G) lod in fp  
(A) "Why" LoD - good in PureScript (explicit imports!) make the usage of modules explicit  

(P) PureScript ala Haskell looks more scary than it is. Also we had more syntax than FP issues.  
Working with existing code makes it easier because you can copy from places. (Maybe related to our level, I assume it would confuse junior people). LoD it is there in a way.  

(A) nice balance Minimal tests (understanding) vs. "Big" tests for refactoring  

(A) Generics in PureScript not intuitive (possible?)  

_About the day as a whole._  

(P) lot of productive time (4x50'), I like it  
Keeping the screen sharing on all time is a great idea.  

(R) Mobbing worked well, time for each person was good fit  
Staying with one exercise for the whole day was good in this case.  

(G) we continued with one exercise the whole day, we do it rarely.  
Learning a new language together works well this way.  

(A) Git Hacking as warmup for session.