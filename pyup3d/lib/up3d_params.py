from enum import IntEnum

class USB_Params():
    VID  = (0x4745)
    PID_MINI_A  = (0x0001)
    PID_MINI_M  = (0x2777)
    PID_PLUS    = (0x277d)
    PID_CETUS_S7  = (0x277f)

class PARA():
    PARA_x01                 = 0x01 #program statusx: 0 = Program Stop, 1 = Program Running, 2 = Program Pause, 3 = Program Have Errors

    PARA_x02                 = 0x02 #MOTOR_1: 0=STOP,1=JOG,2=PROG,3=ERRORSTOP,4=HOMEING,5=ERROR (always 0)
    PARA_x03                 = 0x03 #MOTOR_2: 0=STOP,1=JOG,2=PROG,3=ERRORSTOP,4=HOMEING,5=ERROR (always 0)
    PARA_x04                 = 0x04 #MOTOR_3: 0=STOP,1=JOG,2=PROG,3=ERRORSTOP,4=HOMEING,5=ERROR (always 0)
    PARA_x05                 = 0x05 #MOTOR_4: 0=STOP,1=JOG,2=PROG,3=ERRORSTOP,4=HOMEING,5=ERROR (always 0)

    GET_NOZZLE1_TEMP         = 0x06 #(float)
    GET_NOZZLE2_TEMP         = 0x07 #(float)
    GET_BED_TEMP             = 0x08 #(float)
    GET_TEMP4_TEMP           = 0x09 #(float)

    PARA_REPORT_LAYER        = 0x0A #layer number 1 ..
    PARA_REPORT_HEIGHT       = 0x0B #height 0.01 ..

    PARA_PAUSE_PROGRAM       = 0x0C #pause program
    PARA_x0D                 = 0x0D #stop  program
    PARA_x0E                 = 0x0E #init  program
    PARA_x0F                 = 0x0F #SYSTEM INTERNAL STATUS: 0=NO_ERROR, 1=STOP_AT_LIMIT,
                                   #2=PROGRAM_STOP, 3=OVER_TIME, 4=UNKNOWN_CMD, 5=SINGLE_JOG_CMD, 6=WAIT_PROG_CMD

    PARA_PRINT_STATUS        = 0x10 #STATUS  0=PRINTER ERROR/NOT PRINTING, 1=PREAPRED FOR PRINTING, 2=PRINTING, 3=PAUSED, ...
    PARA_x11                 = 0x11 # 0/1 HAVE SUPPORT / NO SUPPORT ??AFTER EVERY LAYER

    PARA_TEMP_REACHED_N1     = 0x12 # 0/1 N1:  NOT HOT, HOT ENOUGH
    PARA_TEMP_REACHED_N2     = 0x13 # 0/1 N2:  NOT HOT, HOT ENOUGH

    PARA_HEATER_NOZZLE1_ON   = 0x14 #1=ON, >1 n=*2 seconds countdown, 0=OFF
    PARA_HEATER_NOZZLE2_ON   = 0x15 #1=ON, >1 n=*2 seconds countdown, 0=OFF
    PARA_HEATER_BED_ON       = 0x16 #1=ON, >1 n=*2 seconds countdown, 0=OFF

    PARA_x17                 = 0x17 #NOZZLE_OPEN: 0=No Nozzle Open, 1=Nozzle 1 Open, 2=Nozzle 2 Open, 3=2 Nozzles Open

    PARA_x18                 = 0x18 #HF1: %d ?
    PARA_x19                 = 0x19 #HF2: %d ?
    PARA_x1A                 = 0x1A #HF3: %d ?
    PARA_x1B                 = 0x1B #HF4: %d ?

    PARA_x1C                 = 0x1C #PRINTING: 0=Not Printing, 1=Printing

    PARA_x1D                 = 0x1D#Feed Error Length: %d

    PARA_x1E                 = 0x1E #X: 0=X No Error,1=X+ Limit Error, 2=X- Limit Error
    PARA_x1F                 = 0x1F #Y: 0=Y No Error,1=Y+ Limit Error, 2=Y- Limit Error
    PARA_x20                 = 0x20 #Z: 0=Z No Error,1=Z+ Limit Error, 2=Z- Limit Error
    PARA_x21                 = 0x21 #A: 0=A No Error,1=A+ Limit Error, 2=A- Limit Error


    PARA_GET_ENDSTOP_Y       = 0x22 #PL1%d (PositiveLimit1)
    #0x23                            #PL2%d (PositiveLimit2)
    PARA_GET_ENDSTOP_Z       = 0x24 #PL3%d (PositiveLimit3)
    #0x25                            #PL4%d (PositiveLimit4)
    #0x26                            #NL1%d (NegativeLimit1)
    PARA_GET_ENDSTOP_X       = 0x27 #NL2%d (NegativeLimit2)
    #0x28                            #NL3%d (NegativeLimit3)
    #0x29                            #NL4%d (NegativeLimit4)

    #0x2A  5000 | /1000  ==> 5.0     #Change Nozzle Time: %d
    #0x2B  193  | *0.001 ==> 0.193   #Jump Time: %d
    #0x2C                            #Using Nozzle: %d

    PARA_GET_TARGET_TEMP_1   = 0x2D                            #Target Temp 1: %f  (automatic taken after set temp)
    #0x2E                            #Target Temp 2: %f  (automatic taken after set temp)
    #0x2F                            #Target Temp 3: %f  (automatic taken after set temp)
    #0x30                            #Target Temp 4: %f  (automatic taken after set temp)

    #0x31 ?? check door %d
    PARA_LIGHT               = 0x31 #light automatic: 0= turn off after some time, 1=slow go on and go off after some time

    #0x32 ?? 0/1 ?? check 24V power %d

    #0x33 ?? check power key %d
    #0x34 ?? check light key %d

    #0x35 ??  0 ?? check work room fan

    #0x36 ??  103 | *0.001 ==> 0.103  #feedback length

    #0x37 ??  save to sd card
    #0x38 ??  read from sd card

    PARA_NOZZLE1_TEMP        = 0x39 #%d
    PARA_NOZZLE2_TEMP        = 0x3A #%d
    PARA_BED_TEMP            = 0x3B #%d
    #0x3C  TEMP4 TEMP &d
    #0x3E 334/330/306 | *0.01 = 3.34 / 3.30 / 3.06 ==> VERSION ==> same answer as USB-CMD 01 00

    #0x41 ?? 267
    #0x42 ?? 242
    #0x43 ?? 104
    #0x46 ?? 13
    #0x49 ?? 80

    #0x4B ?? (default: 0x1312D00 = 20000000 / 50000000) ? timer base for stepper calculation MHZ of CPU in printer ?

    PARA_REPORT_PERCENT      = 0x4C
    PARA_REPORT_TIME_REMAIN  = 0x4D

    #0x54: UP: "SupportNozzleUpDown" (0x03E8B258 / 0x0000B258)


    #0x82 ?? FF
    #0x83 ?? FF

    #? GET POSITION 0x8C

    PARA_RED_BLUE_BLINK      = 0x8E # RED/BLUE led -1=blue, 0=red, 1=purple, 2-... = blink speed

    #0x94: UP:"SetZPrecision" (0/999)
    # ACCURACY FOR REPORTING AXIS POSITION 999 = best
    #0x94 ?? 0x03e7 / 0x63 ==> 999, 99 ... 0

    #0xB1 FRONT BUTTON STATE  0=DEPRESSED / !0=PRESSED

    #0xBC light countdown timer

    #0xC9, used as counter
    #  UP3D_SetParameter(0x94,999); //set best accuracy for reporting position

class AXIS:
    X_axis = 1
    Y_axis = 2
    Z_axis = 3
    E_axis = 4


class MachineState(IntEnum):
    system_error = 0
    jogging = 1
    running_program = 2
    idle = 3
    unknown_status=4

class ProgramState(IntEnum):
    stop = 0
    running = 1
    pause = 2
    have_errors =3

class SystemState(IntEnum):
    unknown = 0
    system_ready = 1
    running = 2
    paused = 3
    nozzle_error = 5
    motion_error = 6
    print_finished = 7
    user_canceled = 8
    nozzle_to_hot = 9
    nozzle_to_cool = 10
    platform_to_hot = 11
    dip_error = 12
    sweep_error = 13
    scan_error = 14
    scan_calib_error = 15
    system_power_on = 16
    card_error = 17
    sd_card_write_error = 18
    sd_card_read_error = 19
    save_to_sd_card = 20
    jogcmd_error = 21
    invalid_copyright = 22
    over_usage_restriction = 23
    unknown_error = 24

