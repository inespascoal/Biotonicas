var myCharacteristic;

async function onStartButtonClick() {
  let serviceUuid = '6f30b86e-bb28-48a6-b68d-4ae2e60e512a';
  if (serviceUuid.startsWith('0x')) { // para verificar se é um número hexadecimal
    serviceUuid = parseInt(serviceUuid); // converte uma string num inteiro, se não for especificada nenhuma base,é assumida base 10 por default
  }

  let characteristicUuid = '14181dce-eb95-46c5-8431-3b4fe0e0a12d';
  if (characteristicUuid.startsWith('0x')) {
    characteristicUuid = parseInt(characteristicUuid);
  }

  try {
    console.log('Requesting Bluetooth Device...');
    const device = await navigator.bluetooth.requestDevice({
        filters: [{services: [serviceUuid]}]});

    console.log('Connecting to GATT Server...');
    const server = await device.gatt.connect();

    console.log('Getting Service...');
    const service = await server.getPrimaryService(serviceUuid);

    console.log('Getting Characteristic...');
    myCharacteristic = await service.getCharacteristic(characteristicUuid);

    await myCharacteristic.startNotifications();

    console.log('> Notifications started');
    myCharacteristic.addEventListener('characteristicvaluechanged',
        handleNotifications);
  } catch(error) {
    console.log('Argh! ' + error);
  }
}

async function onStopButtonClick() {
  if (myCharacteristic) {
    try {
      await myCharacteristic.stopNotifications();
      console.log('> Notifications stopped');
      myCharacteristic.removeEventListener('characteristicvaluechanged',
          handleNotifications);
    } catch(error) {
      console.log('Argh! ' + error);
    }
  }
}

function handleNotifications(event) {
  let value = event.target.value;
  let buffer = new ArrayBuffer(4);
  let view = new DataView(buffer);
  let float = 0;

  let a = [];
  let aux1 = [];
  let aux2 = [];
  let acc = [];
  let gyr = [];

  let sum_ax = 0;
  let sum_ay = 0;
  let sum_az = 0;

  let ax_mean = 0;
  let ay_mean = 0;
  let az_mean = 0;

  let AX = 0;
  let AY = 0;
  let AZ = 0;

  let increment = 11;
  let numValues = 3;

  let increment_mean = 3;

  let acc_angles = [];

  // Descoficação de bytes para floats
  for (let i = 0; i < value.byteLength; i += 4) {
    byte1 = value.getUint8(i);
    byte2 = value.getUint8(i+1);
    byte3 = value.getUint8(i+2);
    byte4 = value.getUint8(i+3);

    view.setUint8(0, byte1);
    view.setUint8(1, byte2);
    view.setUint8(2, byte3);
    view.setUint8(3, byte4);
    
    float = view.getFloat32(0, true);
    a.push(float);
  }


  // Acelerómetro
  for (let i = 0; i < a.length; i += 11) {
    aux1 = a.slice (i, i + 3);
    acc.push(aux1);
    acc = acc.flat();
  }
  console.log(acc);

  // Giroscópio
  for (let i = 3; i < a.length; i += 11) {
    aux2 = a.slice(i, i+3);
    gyr.push(aux2);
    gyr = gyr.flat();
  }
  console.log(gyr);
 

  // Conversão dados acelerómetro - PARA REVER
  //média ax
  for (let i = 0; i < acc.length; i += 3) {
   sum_ax = acc[i] + sum_ax;
   ax_mean = sum_ax / 5;
  }
  console.log(ax_mean);

  // média ay
  for (let i = 1; i < acc.length; i += 3) {
   sum_ay = acc[i] + sum_ay;
   ay_mean = sum_ay / 5;
  }
  console.log(ay_mean);

  // média az
  for (let i = 2; i < acc.length; i += increment_mean) {
   sum_az = acc[i] + sum_az;
   az_mean = sum_az / 5;
  }
  console.log(az_mean);


  AX = Math.atan(ax_mean / (Math.sqrt(Math.abs(az_mean)) + Math.sqrt(Math.abs(ay_mean))));
  acc_angles.push(AX);
  AY = Math.atan(ay_mean / (Math.sqrt(Math.abs(az_mean)) + Math.sqrt(Math.abs(ax_mean))));
  acc_angles.push(AY);
  AZ = Math.atan(az_mean / (Math.sqrt(Math.abs(ax_mean)) + Math.sqrt(Math.abs(ay_mean))));
  acc_angles.push(AZ);

  console.log(acc_angles);


}