def poorbottle():
  i01.setHandSpeed("left", 0.60, 0.60, 0.60, 0.60, 0.60, 0.60)
  i01.setHandSpeed("right", 0.60, 0.80, 0.60, 0.60, 0.60, 0.60)
  i01.setArmSpeed("left", 0.60, 0.60, 0.65, 0.60)
  i01.setArmSpeed("right", 0.60, 0.60, 0.60, 0.60)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(0,92)
  i01.setTorsoSpeed(1.0,1.0,1.0)
  i01.moveArm("left",55,40,94,55)
  i01.moveArm("right",80,62,38,10)
  i01.moveHand("left",180,140,150,164,180,0)
  i01.moveHand("right",145,112,127,105,143,150)
  i01.moveTorso(90,90,90)

