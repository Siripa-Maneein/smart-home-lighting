// import React from "react";
// import { Button, Collapse } from "react-bootstrap";
// import "../App.css ";
import React, { useState } from "react";
import "./Remote.css";
import axios from "axios";
import { useEffect } from "react";

const Remote = () => {
const sim = {
    room_1: {
      room_name: "Kitchen",
      brightness: 0,
      status: true,
      mode: "auto",
    },
    room_2: {
      room_name: "Lounge",
      brightness: 12,
      status: true,
      mode: "manual",
    },
    room_3: {
      room_name: "Master Bedroom",
      brightness: 12,
      status: true,
      mode: "manual",
    },
  };

  const GetData = async () => {
    const baseURL = "192.168.136.167:8000";
    try {
      const response = await axios.get(baseURL);
      console.log(response.data);
      return response.data;
    } catch (err) {
      return null;
    }
  };
  const [data, setData] = useState({});
  const [open, setOpen] = useState(false);
  const [room, setRoom] = useState("name");
  const [mode, setMode] = useState("Manual");
  const [bri, setbri] = useState("100");

  useEffect(() => {
    my_Data();
  }, []);

  const my_Data = async () => {
    try {
      const data_ = await GetData();
      console.log(data_);
    
      setData(data_);
      setOpen(data.status);
      setRoom(data.name);
      setMode(data.mode);
      setbri(data.brightness);
    } catch (e) {
      console.log(e);
    }
  };

  function manageCheck(e) {
    // if (e.target.checked) {
    //   setOpen(false);
    //   console.log(e.target.value);
    // } else {
    //   setOpen(true);
    //   console.log(e.target.value);
    // }
    if (open) {
      setOpen(!open);
      console.log("open");
    } else {
      setOpen(!open);
      console.log("close");
    }
  }
  function checkMode(e) {
    if (mode === "manual") {
      setMode("auto");
      console.log("Manual");
    } else {
      setMode("manual");
      console.log("auto");
    }
    // if (open) {
    //   setOpen(!open);
    //   console.log("open");
    // } else {
    //   setOpen(!open);
    //   console.log("close");
  }


return (
  <>
  <div className="container">
    <img className ="picture-center"src="https://slideplayer.in.th/slide/2183884/9/images/4/%E0%B8%84%E0%B8%B3%E0%B8%AA%E0%B8%87%E0%B8%A7%E0%B8%99%E0%B9%83%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2+JavaScript.jpg" />
    <div> Name Room : {sim.room_1.room_name} </div>
    <div> Status : {open ? "on" : "off"}</div>
    <div> Mode : {mode==="auto" ? "auto" : "manual"}</div>
    <div> Brightness : {sim.room_1.brightness}</div>

    <div className="slide-button">
      <button
        onClick={(e) => manageCheck(e)}
        className="slide-button__toggle"
        value={sim.room_1.status}
      >
        Staus
      </button>
      <div className="slide-button">
        <button
          onClick={(e) => checkMode(e)}
          className="slide-button__toggle"
          value={sim["room_1"].mode}
        >
          Mode
        </button>
        
      </div>
    </div>
  </div>
  </>
);
};
export default Remote;
