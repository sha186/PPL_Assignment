
flight(barcelona,iberia,valencia,110,75).
flight(paris,united,toulouse,35,120).
flight(barcelona,iberia,london,220,240).
flight(toronto,airCanada,madrid,900,480).
flight(toronto,united,madrid,950,540).
flight(toronto,iberia,madrid,800,480).
flight(toronto,airCanada,london,500,360).
flight(toronto,united,london,650,420).
flight(madrid,airCanada,barcelona,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(madrid,iberia,malaga,50,60).
flight(madrid,iberia,valencia,40,50).
flight(malaga,iberia,valencia,80,120).

airport(toronto,50,60).
airport(madrid,75,45).
airport(valencia,40,20).
airport(malaga,50,30).
airport(barcelona,40,30).
airport(paris,50,60).
airport(london,75,80).
airport(toulouse,40,30).

isFlightExist(A, B):-flight(A, _, B, _, _);flight(B, _, A, _, _).

isFlightCheap(A,C,B):- flight(A,C,B,P,_), P<400.
isTwoFlight(A, B):- isFlightExist(A, X), isFlightExist(X,B).
isPreferred(A, C, B):- C == airCanada; isFlightCheap(A, C, B).

isFlightUnited(A, B):- flight(A, C, B, _, _), C == united.
isFlightCanada(A, B):-  isFlightUnited(A, B).

flightPrint(A, C, B, P, D) :-
    flight(A, C, B, P, D),
    write('A = '),
    write(B),
    nl,
    write('C = '),
    write(C),
    nl,
    write('B = '),
    write(A),
    nl,
    write('P = '),
    write(P),
    write($),
    nl,
    write('D = '),
    write(D),
    write(m),
    nl.




