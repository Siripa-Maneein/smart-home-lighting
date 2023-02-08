import axios from "axios";

export const GetData = async () => {
  const baseURL = "http://127.0.0.1:8000/room/get_info/";
  try {
    const response = await axios.get(baseURL);
    console.log(response.data);
    return response.data;
  } catch (err) {
    return null;
  }
};
