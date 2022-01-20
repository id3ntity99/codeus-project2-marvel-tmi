import axios from "axios";

const BASE_URL = "https://marveltmi.com";

const headers = {
  "X-API-key": `${process.env.REACT_APP_API_KEY}`,
};

export const fetcherAvengers = async () => {
  const { data } = await axios.get(`${BASE_URL}/api/avengers/all`, { headers });
  return data;
};
