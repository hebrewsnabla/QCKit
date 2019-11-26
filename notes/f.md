# I/O
## getarg
```Fortran
call getarg(n,buff) ! n-th arg -> buff
N = iargc()         ! number of args
```
## OPEN
```Fortran
OPEN(UNIT=..., FILE=...)
! UNIT: int
! use NEWUNIT to prevent overlap 
CLOSE(UNIT=...)
```
## READ, WRITE
```Fortran
READ(*,*) buff  ! First star: UNIT, default is 5 (keyboard)
WRITE(*,*) buff ! First star: UNIT, default is 6 (screen)
! Second star: FORMAT

```

# Misc
## 续行符
```Fortran
subroutine h1e(aaa,bbb,ccc, &
ddd,eee,fff)
```

