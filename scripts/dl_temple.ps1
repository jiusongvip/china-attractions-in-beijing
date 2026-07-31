$url = "https://sns-webpic-qc.xhscdn.com/202607311747/264dfba7452954388692d04c086a17e0/note_pre_post_uhdr/1040g3r83233cr5eb07ke05paopp625peq86lhdo8!nd_dft_wlteh_webp_3"
$out = "public/images/attractions/temple-of-heaven.webp"
try {
    $r = Invoke-WebRequest -Uri $url -Headers @{
        "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        "Referer" = "https://www.xiaohongshu.com/"
        "Accept" = "image/webp,image/avif,image/*,*/*;q=0.8"
        "Origin" = "https://www.xiaohongshu.com"
        "Sec-Fetch-Site" = "cross-site"
        "Sec-Fetch-Dest" = "image"
        "Sec-Fetch-Mode" = "no-cors"
    } -OutFile $out -PassThru
    Write-Host "OK: $($r.StatusCode) $((Get-Item $out).Length) bytes"
} catch {
    Write-Host "FAIL: $_"
    # try without suffix
    $url2 = "https://sns-webpic-qc.xhscdn.com/202607311747/264dfba7452954388692d04c086a17e0/note_pre_post_uhdr/1040g3r83233cr5eb07ke05paopp625peq86lhdo8"
    try {
        $r2 = Invoke-WebRequest -Uri $url2 -Headers @{
            "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            "Referer" = "https://www.xiaohongshu.com/"
        } -OutFile $out -PassThru
        Write-Host "OK (no suffix): $($r2.StatusCode) $((Get-Item $out).Length) bytes"
    } catch {
        Write-Host "FAIL (no suffix): $_"
    }
}
