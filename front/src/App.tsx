import { QueryClient, QueryClientProvider } from "react-query";
import { ThemeProvider } from "styled-components";
import { GlobalStyle } from "./styles/global-style";
import { ReactQueryDevtools } from "react-query/devtools";
import { theme } from "./styles/theme";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <GlobalStyle />
        <ReactQueryDevtools initialIsOpen={true} />
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
