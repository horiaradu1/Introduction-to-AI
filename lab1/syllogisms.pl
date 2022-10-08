% -- Exercise 1 --

opposite(+A, -A).
opposite(-A, +A).


% -- Exercise 2 --

if_all(All):-
    % Constrict all the Universal formulas
    All =.. [Formula,_ ,_ ],
    Formula == all.

if_some(Some):-
    % Constrict all the Existential formulas
    Some =.. [Formula,_ ,_],
    Formula == some.

separate(FList, Ex, Univ):-
    % Using the functions above
    % Select and include only the correct formulas for each list
    include(if_some(), FList, Ex),
    include(if_all(), FList, Univ).


% -- Exercise 3 --

% Formula for Barbara Step
bStep(L, M, UFlas):-
    member(all(L, M), UFlas).

bStep(L, M, UFlas):-
    opposite(L, NotL), % from Exercise 1
    opposite(M, NotM), % from Exercise 1
    member(all(NotM, NotL), UFlas).

% Declaring the Barbara Path
bPath(L, M, _).

bPath(L, L, UFlas, Road).

% Function for Barbara Path
% Using road as to not repeat the path used
bPath(L, M, UFlas, Road):-
    bStep(L, Step, UFlas),
    not(member(Step, Road)),
    bPath(Step, M, UFlas, [Step | Road]).

% Finalizing bPath so that it can be called
bPath(L, M, UFlas):-
    bPath(L, M, UFlas, []).


% -- Exercise 4 --

% Includes separate, opposite and bPath functions from last exercises

% Writing the infCheck functions for the 2 cases of Universal formulas
infCheck(Flas, all(P, L)):-
    separate(Flas, _, UFlas),
    opposite(P, NotP),
    bPath(P, NotP, UFlas).

infCheck(Flas, all(P, L)):-
    separate(Flas, _, UFlas),
    bPath(P, L, UFlas).

% Writing the infCheck functions for the 4 cases of the Existential formulas
infCheck(Flas, some(Q, M)):-
    separate(Flas, EFlas, UFlas),
    member(some(P, L), EFlas),
    bPath(P, Q, UFlas),
    bPath(P, M, UFlas).

infCheck(Flas, some(Q, M)):-
    separate(Flas, EFlas, UFlas),
    member(some(P, L), EFlas),
    bPath(L, Q, UFlas),
    bPath(L, M, UFlas).

infCheck(Flas, some(Q, M)):-
    separate(Flas, EFlas, UFlas),
    member(some(P, L), EFlas),
    bPath(P, Q, UFlas),
    bPath(L, M, UFlas).

infCheck(Flas, some(Q, M)):-
    separate(Flas, EFlas, UFlas),
    member(some(P, L), EFlas),
    bPath(L, Q, UFlas),
    bPath(P, M, UFlas).