import { useQuery } from "react-query";
import Avenger from "../../components/Avenger";
import Header from "../../components/header";
import { IavengersInfo } from "../../typings/db";
import { fetcherAvengers } from "../../utils/api";
import { PostWrapper } from "./styles";

const Home = () => {
  const { isLoading, data: avengersData } = useQuery<IavengersInfo[]>(
    "allAvengers",
    fetcherAvengers,
    { refetchOnWindowFocus: false }
  );
  console.log(avengersData);
  return (
    <>
      {isLoading ? (
        "loading..."
      ) : (
        <>
          <Header />
          <PostWrapper>
            {avengersData?.map(avenger => (
              <Avenger key={avenger.id} avengerInfo={avenger} />
            ))}
          </PostWrapper>
        </>
      )}
    </>
  );
};

export default Home;
